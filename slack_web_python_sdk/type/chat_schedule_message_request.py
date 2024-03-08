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


class RequiredChatScheduleMessageRequest(TypedDict):
    pass

class OptionalChatScheduleMessageRequest(TypedDict, total=False):
    # Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See [chat.postMessage](chat.postMessage#authorship).
    as_user: bool

    # A JSON-based array of structured attachments, presented as a URL-encoded string.
    attachments: str

    # A JSON-based array of structured blocks, presented as a URL-encoded string.
    blocks: str

    # Channel, private group, or DM channel to send message to. Can be an encoded ID, or a name. See [below](https://slack.dev) for more details.
    channel: str

    # Find and link channel names and usernames.
    link_names: bool

    # Change how messages are treated. Defaults to `none`. See [chat.postMessage](chat.postMessage#formatting).
    parse: str

    # Unix EPOCH timestamp of time in future to send the message.
    post_at: str

    # Used in conjunction with `thread_ts` and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to `false`.
    reply_broadcast: bool

    # How this field works and whether it is required depends on other fields you use in your API call. [See below](https://slack.dev) for more detail.
    text: str

    # Provide another message's `ts` value to make this message a reply. Avoid using a reply's `ts` value; use its parent instead.
    thread_ts: typing.Union[int, float]

    # Pass true to enable unfurling of primarily text-based content.
    unfurl_links: bool

    # Pass false to disable unfurling of media content.
    unfurl_media: bool

class ChatScheduleMessageRequest(RequiredChatScheduleMessageRequest, OptionalChatScheduleMessageRequest):
    pass
