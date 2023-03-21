"""Backend server."""
from collections.abc import Mapping
from enum import Enum
from typing import Annotated, Any

from fastapi import Depends, FastAPI, Header, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from structlog import get_logger

from stock_monitor_backend.notifyer import NotificationCenter
from stock_monitor_backend.rules import asr_rule
from stock_monitor_backend.telegram.client import TelegramClient, Update


class BotAction(str, Enum):
    """Supported action names."""
    ASR_REMINDER = "action_react_to_asr_reminder"


class CustomRasaBotMessage(BaseModel):
    """Rasa's bot message JSON format."""
    name: BotAction
    entities: Mapping[str, Any]


class RasaBotMessage(BaseModel):
    """Rasa's bot message."""
    custom: CustomRasaBotMessage


def create_app(telegram_bot_token: str) -> FastAPI:
    """Creates and web server based on the FastAPI."""
    app = FastAPI(openapi_url="/api/openapi.json")
    logger = get_logger()

    telegram_client = TelegramClient(token=telegram_bot_token)
    notify = NotificationCenter()
    notify.add_telegram(telegram_client)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
        exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
        logger.error(f"{request.headers=}: {exc_str}")
        content = {'status_code': 10422, 'message': exc_str, 'data': None}
        return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @app.get("/")
    async def root() -> Mapping[str, str]:
        """ROot."""
        return {"message": "stock monitor backend"}

    @app.post("/rasa/webhook")
    async def rasa_webhook(r: RasaBotMessage) -> Mapping[str, str]:
        """Listens to rasa's messages."""
        match r.custom.name:
            case BotAction.ASR_REMINDER:
                notify.send_unique_decision("dbihbka", asr_rule(r.custom.entities['ticker']))
            case _:
                logger.debug(r)
        return {"message": 'ok'}

    async def verify_telegram_bot_api_secret_token(x_telegram_bot_api_secret_token: Annotated[str, Header()]) -> None:
        """Checks X-Telegram-Bot-Api-Secret-Token."""
        if x_telegram_bot_api_secret_token != telegram_client.secret_token:
            logger.critical("Secret token is invliad. "
                           f"{x_telegram_bot_api_secret_token} != {telegram_client.secret_token}")
            raise HTTPException(status_code=400, detail="X-Telegram-Bot-Api-Secret-Token is invalid.")

    @app.post("/telegram/webhook", dependencies=[Depends(verify_telegram_bot_api_secret_token)])
    async def telegram_webhook(update: Update) -> bool:
        """Listens to telegram's messages."""
        logger.debug(update)
        return True

    telegram_client.set_webhook()
    return app


def main() -> None:
    """Runner."""
    import os

    import uvicorn

    telegram_bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    assert telegram_bot_token, "Missing TELEGRAM_BOT_TOKEN"

    uvicorn.run(create_app(telegram_bot_token))


if __name__ == "__main__":
    main()
