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


class ReactionsAddRequest(BaseModel):
    # Channel where the message to add reaction to was posted.
    channel: str = Field(alias='channel')

    # Reaction (emoji) name.
    name: str = Field(alias='name')

    # Timestamp of the message to add reaction to.
    timestamp: str = Field(alias='timestamp')
    class Config:
        arbitrary_types_allowed = True
