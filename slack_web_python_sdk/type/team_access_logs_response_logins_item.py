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

from slack_web_python_sdk.type.defs_user_id import DefsUserId

class RequiredTeamAccessLogsResponseLoginsItem(TypedDict):
    count: int

    country: typing.Optional[str]

    date_first: int

    date_last: int

    ip: typing.Optional[str]

    isp: typing.Optional[str]

    region: typing.Optional[str]

    user_agent: str

    user_id: DefsUserId

    username: str

class OptionalTeamAccessLogsResponseLoginsItem(TypedDict, total=False):
    pass

class TeamAccessLogsResponseLoginsItem(RequiredTeamAccessLogsResponseLoginsItem, OptionalTeamAccessLogsResponseLoginsItem):
    pass
