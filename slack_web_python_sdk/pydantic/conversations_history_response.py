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

from slack_web_python_sdk.pydantic.defs_ok_true import DefsOkTrue
from slack_web_python_sdk.pydantic.objs_message import ObjsMessage

class ConversationsHistoryResponse(BaseModel):
    channel_actions_count: int = Field(alias='channel_actions_count')

    channel_actions_ts: typing.List[typing.Union[typing.List[int], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(alias='channel_actions_ts')

    has_more: bool = Field(alias='has_more')

    messages: typing.List[ObjsMessage] = Field(alias='messages')

    ok: DefsOkTrue = Field(alias='ok')

    pin_count: int = Field(alias='pin_count')
    class Config:
        arbitrary_types_allowed = True
