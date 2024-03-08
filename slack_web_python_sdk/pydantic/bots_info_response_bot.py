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

from slack_web_python_sdk.pydantic.bots_info_response_bot_icons import BotsInfoResponseBotIcons
from slack_web_python_sdk.pydantic.defs_app_id import DefsAppId
from slack_web_python_sdk.pydantic.defs_bot_id import DefsBotId
from slack_web_python_sdk.pydantic.defs_user_id import DefsUserId

class BotsInfoResponseBot(BaseModel):
    app_id: DefsAppId = Field(alias='app_id')

    deleted: bool = Field(alias='deleted')

    icons: BotsInfoResponseBotIcons = Field(alias='icons')

    id: DefsBotId = Field(alias='id')

    name: str = Field(alias='name')

    updated: int = Field(alias='updated')

    user_id: typing.Optional[DefsUserId] = Field(None, alias='user_id')
    class Config:
        arbitrary_types_allowed = True
