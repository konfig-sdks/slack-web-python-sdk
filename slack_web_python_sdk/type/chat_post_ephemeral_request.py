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


class RequiredChatPostEphemeralRequest(TypedDict):
    # Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name.
    channel: str

    # `id` of the user who will receive the ephemeral message. The user should be in the channel specified by the `channel` argument.
    user: str

class OptionalChatPostEphemeralRequest(TypedDict, total=False):
    # Pass true to post the message as the authed user. Defaults to true if the chat:write:bot scope is not included. Otherwise, defaults to false.
    as_user: bool

    # A JSON-based array of structured attachments, presented as a URL-encoded string.
    attachments: str

    # A JSON-based array of structured blocks, presented as a URL-encoded string.
    blocks: str

    # Emoji to use as the icon for this message. Overrides `icon_url`. Must be used in conjunction with `as_user` set to `false`, otherwise ignored. See [authorship](https://slack.dev) below.
    icon_emoji: str

    # URL to an image to use as the icon for this message. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](https://slack.dev) below.
    icon_url: str

    # Find and link channel names and usernames.
    link_names: bool

    # Change how messages are treated. Defaults to `none`. See [below](https://slack.dev).
    parse: str

    # How this field works and whether it is required depends on other fields you use in your API call. [See below](https://slack.dev) for more detail.
    text: str

    # Provide another message's `ts` value to post this message in a thread. Avoid using a reply's `ts` value; use its parent's value instead. Ephemeral messages in threads are only shown if there is already an active thread.
    thread_ts: str

    # Set your bot's user name. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](https://slack.dev) below.
    username: str

class ChatPostEphemeralRequest(RequiredChatPostEphemeralRequest, OptionalChatPostEphemeralRequest):
    pass
