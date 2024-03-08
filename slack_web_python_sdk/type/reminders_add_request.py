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


class RequiredRemindersAddRequest(TypedDict):
    # The content of the reminder
    text: str

    # When this reminder should happen: the Unix timestamp (up to five years from now), the number of seconds until the reminder (if within 24 hours), or a natural language description (Ex. \"in 15 minutes,\" or \"every Thursday\")
    time: str

class OptionalRemindersAddRequest(TypedDict, total=False):
    # The user who will receive the reminder. If no user is specified, the reminder will go to user who created it.
    user: str

class RemindersAddRequest(RequiredRemindersAddRequest, OptionalRemindersAddRequest):
    pass
