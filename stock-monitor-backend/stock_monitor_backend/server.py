"""Backend server."""

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from h2o_lightwave import wave_serve
from h2o_lightwave_web import web_directory

from structlog import get_logger

from stock_monitor_backend.wave import serve


def create_app() -> FastAPI:
    """Creates and web server based on the FastAPI."""

    app = FastAPI(openapi_url="/api/openapi.json")
    logger = get_logger()

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
        exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
        logger.error(f"{request.headers=}: {exc_str}")
        content = {'status_code': 10422, 'message': exc_str, 'data': None}
        return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @app.websocket("/_s/")
    async def ws(ws: WebSocket):
        try:
            await ws.accept()
            await wave_serve(serve, ws.send_text, ws.receive_text)
            await ws.close()
        except WebSocketDisconnect as e:
            logger.info(f"Client disconnected. {repr(e)}")

    app.mount("/", StaticFiles(directory=web_directory, html=True), name="/")
    return app


def main() -> None:
    """Runner."""
    import uvicorn

    uvicorn.run("stock_monitor_backend.server:create_app", workers=2, lifespan="on", log_level="info")
