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

from slack_web_python_sdk.pydantic.defs_app_id import DefsAppId
from slack_web_python_sdk.pydantic.defs_channel import DefsChannel
from slack_web_python_sdk.pydantic.defs_user_id import DefsUserId

class TeamIntegrationLogsResponseLogsItem(BaseModel):
    app_id: DefsAppId = Field(alias='app_id')

    app_type: str = Field(alias='app_type')

    change_type: str = Field(alias='change_type')

    date: str = Field(alias='date')

    scope: str = Field(alias='scope')

    user_id: DefsUserId = Field(alias='user_id')

    user_name: str = Field(alias='user_name')

    admin_app_id: typing.Optional[DefsAppId] = Field(None, alias='admin_app_id')

    channel: typing.Optional[DefsChannel] = Field(None, alias='channel')

    service_id: typing.Optional[str] = Field(None, alias='service_id')

    service_type: typing.Optional[str] = Field(None, alias='service_type')
    class Config:
        arbitrary_types_allowed = True
