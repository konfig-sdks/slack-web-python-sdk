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


class RequiredChatUpdateRequest(TypedDict):
    # Channel containing the message to be updated.
    channel: str

    # Timestamp of the message to be updated.
    ts: str

class OptionalChatUpdateRequest(TypedDict, total=False):
    # Pass true to update the message as the authed user. [Bot users](https://slack.dev) in this context are considered authed users.
    as_user: str

    # A JSON-based array of structured attachments, presented as a URL-encoded string. This field is required when not presenting `text`. If you don't include this field, the message's previous `attachments` will be retained. To remove previous `attachments`, include an empty array for this field.
    attachments: str

    # A JSON-based array of [structured blocks](https://slack.dev), presented as a URL-encoded string. If you don't include this field, the message's previous `blocks` will be retained. To remove previous `blocks`, include an empty array for this field.
    blocks: str

    # Find and link channel names and usernames. Defaults to `none`. If you do not specify a value for this field, the original value set for the message will be overwritten with the default, `none`.
    link_names: str

    # Change how messages are treated. Defaults to `client`, unlike `chat.postMessage`. Accepts either `none` or `full`. If you do not specify a value for this field, the original value set for the message will be overwritten with the default, `client`.
    parse: str

    # New text for the message, using the [default formatting rules](https://slack.dev). It's not required when presenting `blocks` or `attachments`.
    text: str

class ChatUpdateRequest(RequiredChatUpdateRequest, OptionalChatUpdateRequest):
    pass
