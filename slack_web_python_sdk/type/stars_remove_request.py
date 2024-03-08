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


class RequiredStarsRemoveRequest(TypedDict):
    pass

class OptionalStarsRemoveRequest(TypedDict, total=False):
    # Channel to remove star from, or channel where the message to remove star from was posted (used with `timestamp`).
    channel: str

    # File to remove star from.
    file: str

    # File comment to remove star from.
    file_comment: str

    # Timestamp of the message to remove star from.
    timestamp: str

class StarsRemoveRequest(RequiredStarsRemoveRequest, OptionalStarsRemoveRequest):
    pass
