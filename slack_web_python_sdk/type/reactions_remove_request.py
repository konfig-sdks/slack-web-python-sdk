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


class RequiredReactionsRemoveRequest(TypedDict):
    # Reaction (emoji) name.
    name: str

class OptionalReactionsRemoveRequest(TypedDict, total=False):
    # Channel where the message to remove reaction from was posted.
    channel: str

    # File to remove reaction from.
    file: str

    # File comment to remove reaction from.
    file_comment: str

    # Timestamp of the message to remove reaction from.
    timestamp: str

class ReactionsRemoveRequest(RequiredReactionsRemoveRequest, OptionalReactionsRemoveRequest):
    pass
