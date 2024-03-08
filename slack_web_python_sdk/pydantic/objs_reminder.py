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

from slack_web_python_sdk.pydantic.defs_reminder_id import DefsReminderId
from slack_web_python_sdk.pydantic.defs_user_id import DefsUserId

class ObjsReminder(BaseModel):
    creator: DefsUserId = Field(alias='creator')

    id: DefsReminderId = Field(alias='id')

    recurring: bool = Field(alias='recurring')

    text: str = Field(alias='text')

    user: DefsUserId = Field(alias='user')

    complete_ts: typing.Optional[int] = Field(None, alias='complete_ts')

    time: typing.Optional[int] = Field(None, alias='time')
    class Config:
        arbitrary_types_allowed = True
