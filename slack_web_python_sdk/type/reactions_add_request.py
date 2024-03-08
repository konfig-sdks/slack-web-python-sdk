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


class RequiredReactionsAddRequest(TypedDict):
    # Channel where the message to add reaction to was posted.
    channel: str

    # Reaction (emoji) name.
    name: str

    # Timestamp of the message to add reaction to.
    timestamp: str

class OptionalReactionsAddRequest(TypedDict, total=False):
    pass

class ReactionsAddRequest(RequiredReactionsAddRequest, OptionalReactionsAddRequest):
    pass
