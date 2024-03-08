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

from slack_web_python_sdk.pydantic.defs_user_id import DefsUserId

class TeamAccessLogsResponseLoginsItem(BaseModel):
    count: int = Field(alias='count')

    country: typing.Optional[str] = Field(alias='country')

    date_first: int = Field(alias='date_first')

    date_last: int = Field(alias='date_last')

    ip: typing.Optional[str] = Field(alias='ip')

    isp: typing.Optional[str] = Field(alias='isp')

    region: typing.Optional[str] = Field(alias='region')

    user_agent: str = Field(alias='user_agent')

    user_id: DefsUserId = Field(alias='user_id')

    username: str = Field(alias='username')
    class Config:
        arbitrary_types_allowed = True
