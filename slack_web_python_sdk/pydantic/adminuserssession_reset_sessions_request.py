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


class AdminuserssessionResetSessionsRequest(BaseModel):
    # The ID of the user to wipe sessions for
    user_id: str = Field(alias='user_id')

    # Only expire mobile sessions (default: false)
    mobile_only: typing.Optional[bool] = Field(None, alias='mobile_only')

    # Only expire web sessions (default: false)
    web_only: typing.Optional[bool] = Field(None, alias='web_only')
    class Config:
        arbitrary_types_allowed = True
