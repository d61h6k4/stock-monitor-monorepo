"""Telegram client implementation."""
from typing import Optional, Self
from uuid import uuid4

from pydantic import BaseModel, Field
from requests import Session
from logging import getLogger

logger = getLogger(__name__)


class User(BaseModel):
    """User object.

    See: https://core.telegram.org/bots/api#user
    """

    user_id: int = Field(alias="id")
    is_bot: bool
    first_name: str
    last_name: str | None
    username: str | None
    language_code: str | None
    is_premium: bool | None
    added_to_attachment_menu: bool | None
    can_join_groups: bool | None
    can_read_all_group_messages: bool | None
    supports_inline_queries: bool | None


class Chat(BaseModel):
    """Chat object.

    See: https://core.telegram.org/bots/api#chat
    """

    chat_id: int = Field(alias="id")
    chat_type: str = Field(alias="type")
    title: str | None
    username: str | None
    first_name: str | None
    last_name: str | None
    is_forum: bool | None


class Message(BaseModel):
    """Message object.

    See: https://core.telegram.org/bots/api#message
    """

    message_id: int
    message_thread_id: int | None
    from_user: User | None = Field(alias="from")
    sender_chat: Chat | None
    date: int
    chat: Chat
    forward_from: User | None
    forward_from_chat: Chat | None
    forward_from_message_id: int | None
    forward_signature: str | None
    forward_sender_name: str | None
    forward_date: int | None
    is_topic_message: bool | None
    is_automatic_forward: bool | None
    reply_to_message: Optional["Message"]
    via_bot: User | None
    edit_date: int | None
    has_protected_content: bool | None
    media_group_id: str | None
    author_signature: str | None
    text: str | None
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
    message: Message | None
    edited_message: Message | None
    channel_post: Message | None
    edited_channel_post: Message | None


class TelegramClient:
    """Telegram client object."""

    def __init__(self: Self, token: str) -> None:
        """Constructor."""
        self._telegram_api_url = f"https://api.telegram.org/bot{token}"
        self.secret_token = uuid4().hex
        self.session = Session()

    def set_webhook(self: Self) -> None:
        """Sets webhook.

        Configures where Telegram server can send update messages.
        """

        r = self.session.post(
            url=f"{self._telegram_api_url}/setWebhook",
            data={
                "url": "https://lochaufwallstrasse.de/api/telegram/webhook",
                "secret_token": self.secret_token,
            },
        )
        r.raise_for_status()

    def send_message(self: Self, chat_id: int, text: str) -> None:
        """Sends message."""
        payload = {"chat_id": chat_id, "text": text, "parse_mode": "MarkdownV2"}
        r = self.session.post(url=f"{self._telegram_api_url}/sendMessage", data=payload)
        if not r.ok:
            logger.critical(
                f"sendMessage with {payload} failed with {r.status_code} {r.content}"
            )

        r.raise_for_status()
