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

from slack_web_python_sdk.pydantic.defs_channel_id import DefsChannelId

class ChatscheduledMessagesListResponseScheduledMessagesItem(BaseModel):
    channel_id: DefsChannelId = Field(alias='channel_id')

    date_created: int = Field(alias='date_created')

    id: str = Field(alias='id')

    post_at: int = Field(alias='post_at')

    text: typing.Optional[str] = Field(None, alias='text')
    class Config:
        arbitrary_types_allowed = True
