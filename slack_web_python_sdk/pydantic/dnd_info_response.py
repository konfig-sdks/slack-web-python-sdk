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

class DndInfoResponse(BaseModel):
    dnd_enabled: bool = Field(alias='dnd_enabled')

    next_dnd_end_ts: int = Field(alias='next_dnd_end_ts')

    next_dnd_start_ts: int = Field(alias='next_dnd_start_ts')

    ok: DefsOkTrue = Field(alias='ok')

    snooze_enabled: typing.Optional[bool] = Field(None, alias='snooze_enabled')

    snooze_endtime: typing.Optional[int] = Field(None, alias='snooze_endtime')

    snooze_remaining: typing.Optional[int] = Field(None, alias='snooze_remaining')
    class Config:
        arbitrary_types_allowed = True
