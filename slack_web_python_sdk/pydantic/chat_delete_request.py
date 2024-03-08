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


class ChatDeleteRequest(BaseModel):
    # Pass true to delete the message as the authed user with `chat:write:user` scope. [Bot users](https://slack.dev) in this context are considered authed users. If unused or false, the message will be deleted with `chat:write:bot` scope.
    as_user: typing.Optional[bool] = Field(None, alias='as_user')

    # Channel containing the message to be deleted.
    channel: typing.Optional[str] = Field(None, alias='channel')

    # Timestamp of the message to be deleted.
    ts: typing.Optional[typing.Union[int, float]] = Field(None, alias='ts')
    class Config:
        arbitrary_types_allowed = True
