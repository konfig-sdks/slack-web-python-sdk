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
from slack_web_python_sdk.pydantic.defs_team import DefsTeam
from slack_web_python_sdk.pydantic.defs_user_id import DefsUserId
from slack_web_python_sdk.pydantic.objs_bot_profile import ObjsBotProfile

class ChatScheduleMessageResponseMessage(BaseModel):
    bot_id: DefsBotId = Field(alias='bot_id')

    team: DefsTeam = Field(alias='team')

    text: str = Field(alias='text')

    type: str = Field(alias='type')

    user: DefsUserId = Field(alias='user')

    bot_profile: typing.Optional[ObjsBotProfile] = Field(None, alias='bot_profile')

    username: typing.Optional[str] = Field(None, alias='username')
    class Config:
        arbitrary_types_allowed = True
