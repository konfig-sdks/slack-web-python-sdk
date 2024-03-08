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


class StarsRemoveRequest(BaseModel):
    # Channel to remove star from, or channel where the message to remove star from was posted (used with `timestamp`).
    channel: typing.Optional[str] = Field(None, alias='channel')

    # File to remove star from.
    file: typing.Optional[str] = Field(None, alias='file')

    # File comment to remove star from.
    file_comment: typing.Optional[str] = Field(None, alias='file_comment')

    # Timestamp of the message to remove star from.
    timestamp: typing.Optional[str] = Field(None, alias='timestamp')
    class Config:
        arbitrary_types_allowed = True
