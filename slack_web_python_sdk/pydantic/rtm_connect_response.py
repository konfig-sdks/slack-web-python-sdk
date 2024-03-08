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
from slack_web_python_sdk.pydantic.rtm_connect_response_self import RtmConnectResponseSelf
from slack_web_python_sdk.pydantic.rtm_connect_response_team import RtmConnectResponseTeam

class RtmConnectResponse(BaseModel):
    ok: DefsOkTrue = Field(alias='ok')

    self_: RtmConnectResponseSelf = Field(alias='self')

    team: RtmConnectResponseTeam = Field(alias='team')

    url: str = Field(alias='url')
    class Config:
        arbitrary_types_allowed = True
