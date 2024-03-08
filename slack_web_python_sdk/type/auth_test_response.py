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

from slack_web_python_sdk.type.defs_bot_id import DefsBotId
from slack_web_python_sdk.type.defs_ok_true import DefsOkTrue
from slack_web_python_sdk.type.defs_team import DefsTeam
from slack_web_python_sdk.type.defs_user_id import DefsUserId

class RequiredAuthTestResponse(TypedDict):
    ok: DefsOkTrue

    team: str

    team_id: DefsTeam

    url: str

    user: str

    user_id: DefsUserId

class OptionalAuthTestResponse(TypedDict, total=False):
    bot_id: DefsBotId

    is_enterprise_install: bool

class AuthTestResponse(RequiredAuthTestResponse, OptionalAuthTestResponse):
    pass
