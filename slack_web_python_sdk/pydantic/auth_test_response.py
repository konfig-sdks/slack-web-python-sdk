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
from pydantic import BaseModel, Field, RootModel

from slack_web_python_sdk.pydantic.defs_bot_id import DefsBotId
from slack_web_python_sdk.pydantic.defs_ok_true import DefsOkTrue
from slack_web_python_sdk.pydantic.defs_team import DefsTeam
from slack_web_python_sdk.pydantic.defs_user_id import DefsUserId

class AuthTestResponse(BaseModel):
    ok: DefsOkTrue = Field(alias='ok')

    team: str = Field(alias='team')

    team_id: DefsTeam = Field(alias='team_id')

    url: str = Field(alias='url')

    user: str = Field(alias='user')

    user_id: DefsUserId = Field(alias='user_id')

    bot_id: typing.Optional[DefsBotId] = Field(None, alias='bot_id')

    is_enterprise_install: typing.Optional[bool] = Field(None, alias='is_enterprise_install')
    class Config:
        arbitrary_types_allowed = True
