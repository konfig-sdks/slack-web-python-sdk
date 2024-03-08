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


class RequiredConversationsMarkRequest(TypedDict):
    pass

class OptionalConversationsMarkRequest(TypedDict, total=False):
    # Channel or conversation to set the read cursor for.
    channel: str

    # Unique identifier of message you want marked as most recently seen in this conversation.
    ts: typing.Union[int, float]

class ConversationsMarkRequest(RequiredConversationsMarkRequest, OptionalConversationsMarkRequest):
    pass
