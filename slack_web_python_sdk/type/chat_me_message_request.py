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


class RequiredChatMeMessageRequest(TypedDict):
    pass

class OptionalChatMeMessageRequest(TypedDict, total=False):
    # Channel to send message to. Can be a public channel, private group or IM channel. Can be an encoded ID, or a name.
    channel: str

    # Text of the message to send.
    text: str

class ChatMeMessageRequest(RequiredChatMeMessageRequest, OptionalChatMeMessageRequest):
    pass
