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


class ChatPostMessageRequest(BaseModel):
    # Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. See [below](https://slack.dev) for more details.
    channel: str = Field(alias='channel')

    # Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See [authorship](https://slack.dev) below.
    as_user: typing.Optional[str] = Field(None, alias='as_user')

    # A JSON-based array of structured attachments, presented as a URL-encoded string.
    attachments: typing.Optional[str] = Field(None, alias='attachments')

    # A JSON-based array of structured blocks, presented as a URL-encoded string.
    blocks: typing.Optional[str] = Field(None, alias='blocks')

    # Emoji to use as the icon for this message. Overrides `icon_url`. Must be used in conjunction with `as_user` set to `false`, otherwise ignored. See [authorship](https://slack.dev) below.
    icon_emoji: typing.Optional[str] = Field(None, alias='icon_emoji')

    # URL to an image to use as the icon for this message. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](https://slack.dev) below.
    icon_url: typing.Optional[str] = Field(None, alias='icon_url')

    # Find and link channel names and usernames.
    link_names: typing.Optional[bool] = Field(None, alias='link_names')

    # Disable Slack markup parsing by setting to `false`. Enabled by default.
    mrkdwn: typing.Optional[bool] = Field(None, alias='mrkdwn')

    # Change how messages are treated. Defaults to `none`. See [below](https://slack.dev).
    parse: typing.Optional[str] = Field(None, alias='parse')

    # Used in conjunction with `thread_ts` and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to `false`.
    reply_broadcast: typing.Optional[bool] = Field(None, alias='reply_broadcast')

    # How this field works and whether it is required depends on other fields you use in your API call. [See below](https://slack.dev) for more detail.
    text: typing.Optional[str] = Field(None, alias='text')

    # Provide another message's `ts` value to make this message a reply. Avoid using a reply's `ts` value; use its parent instead.
    thread_ts: typing.Optional[str] = Field(None, alias='thread_ts')

    # Pass true to enable unfurling of primarily text-based content.
    unfurl_links: typing.Optional[bool] = Field(None, alias='unfurl_links')

    # Pass false to disable unfurling of media content.
    unfurl_media: typing.Optional[bool] = Field(None, alias='unfurl_media')

    # Set your bot's user name. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](https://slack.dev) below.
    username: typing.Optional[str] = Field(None, alias='username')
    class Config:
        arbitrary_types_allowed = True
