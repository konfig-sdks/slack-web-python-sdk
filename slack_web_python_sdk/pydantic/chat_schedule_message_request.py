# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class ChatScheduleMessageRequest(BaseModel):
    # Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See [chat.postMessage](chat.postMessage#authorship).
    as_user: typing.Optional[bool] = Field(None, alias='as_user')

    # A JSON-based array of structured attachments, presented as a URL-encoded string.
    attachments: typing.Optional[str] = Field(None, alias='attachments')

    # A JSON-based array of structured blocks, presented as a URL-encoded string.
    blocks: typing.Optional[str] = Field(None, alias='blocks')

    # Channel, private group, or DM channel to send message to. Can be an encoded ID, or a name. See [below](https://slack.dev) for more details.
    channel: typing.Optional[str] = Field(None, alias='channel')

    # Find and link channel names and usernames.
    link_names: typing.Optional[bool] = Field(None, alias='link_names')

    # Change how messages are treated. Defaults to `none`. See [chat.postMessage](chat.postMessage#formatting).
    parse: typing.Optional[str] = Field(None, alias='parse')

    # Unix EPOCH timestamp of time in future to send the message.
    post_at: typing.Optional[str] = Field(None, alias='post_at')

    # Used in conjunction with `thread_ts` and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to `false`.
    reply_broadcast: typing.Optional[bool] = Field(None, alias='reply_broadcast')

    # How this field works and whether it is required depends on other fields you use in your API call. [See below](https://slack.dev) for more detail.
    text: typing.Optional[str] = Field(None, alias='text')

    # Provide another message's `ts` value to make this message a reply. Avoid using a reply's `ts` value; use its parent instead.
    thread_ts: typing.Optional[typing.Union[int, float]] = Field(None, alias='thread_ts')

    # Pass true to enable unfurling of primarily text-based content.
    unfurl_links: typing.Optional[bool] = Field(None, alias='unfurl_links')

    # Pass false to disable unfurling of media content.
    unfurl_media: typing.Optional[bool] = Field(None, alias='unfurl_media')
    class Config:
        arbitrary_types_allowed = True
