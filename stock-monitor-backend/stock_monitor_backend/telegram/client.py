from uuid import uuid4
from typing import Optional, Sequence
from pydantic import BaseModel, Field
from requests import Session

from structlog import get_logger

logger = get_logger()


class User(BaseModel):
    """User object.

    See: https://core.telegram.org/bots/api#user
    """
    user_id: int = Field(alias="id")
    is_bot: bool
    first_name: str
    last_name: Optional[str]
    username: Optional[str]
    language_code: Optional[str]
    is_premium: Optional[bool]
    added_to_attachment_menu: Optional[bool]
    can_join_groups: Optional[bool]
    can_read_all_group_messages: Optional[bool]
    supports_inline_queries: Optional[bool]


class Chat(BaseModel):
    """Chat object.

    See: https://core.telegram.org/bots/api#chat
    """
    chat_id: int = Field(alias="id")
    chat_type: str = Field(alias="type")
    title: Optional[str]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    is_forum: Optional[bool]


class Message(BaseModel):
    """Message object.

    See: https://core.telegram.org/bots/api#message
    """
    message_id: int
    message_thread_id: Optional[int]
    from_user: Optional[User] = Field(alias="from")
    sender_chat: Optional[Chat]
    date: int
    chat: Chat
    forward_from: Optional[User]
    forward_from_chat: Optional[Chat]
    forward_from_message_id: Optional[int]
    forward_signature: Optional[str]
    forward_sender_name: Optional[str]
    forward_date: Optional[int]
    is_topic_message: Optional[bool]
    is_automatic_forward: Optional[bool]
    reply_to_message: Optional["Message"]
    via_bot: Optional[User]
    edit_date: Optional[int]
    has_protected_content: Optional[bool]
    media_group_id: Optional[str]
    author_signature: Optional[str]
    text: Optional[str]
    # entities: Optional[Sequence[MessageEntity]]
    # animation: Optional[Animation]
    # audio: Optional[Audio]
    # document: Optional[Document]
    # photo: Optional[Sequence[PhotoSize]]
    # sticker: Optional[Sticker]
    # video: Optional[Video]
    # video_note: Optional[VideoNote]
    # voice: Optional[Voice]
    # caption: Optional[str]
    # caption_entities: Optional[Sequence[MessageEntity]]
    # has_media_spoiler: Optional[bool]
    # contact: Optional[Contact]


class Update(BaseModel):
    """Update object.

    See: https://core.telegram.org/bots/api#update
    """
    update_id: int
    message: Optional[Message]
    edited_message: Optional[Message]
    channel_post: Optional[Message]
    edited_channel_post: Optional[Message]


class TelegramClient:
    def __init__(self, token: str):
        self._telegram_api_url = f"https://api.telegram.org/bot{token}"
        self.secret_token = uuid4().hex
        self.session = Session()

    def set_webhook(self):
        r = self.session.post(url=f"{self._telegram_api_url}/setWebhook",
                              data={"url": "https://lochaufwallstrasse.de/api/telegram/webhook",
                                    "secret_token": self.secret_token})
        r.raise_for_status()

    def send_message(self, chat_id: int, text: str):
        payload = {"chat_id": chat_id, "text": text, "parse_mode": "MarkdownV2"}
        r = self.session.post(url=f"{self._telegram_api_url}/sendMessage",
                              data=payload)
        if r.status_code != 200:
            logger.critical(f"sendMessage with {payload} failed with {r.status_code} {r.content}")

        r.raise_for_status()
