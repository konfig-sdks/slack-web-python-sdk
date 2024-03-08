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


class ObjsMessageIcons(BaseModel):
    emoji: typing.Optional[str] = Field(None, alias='emoji')

    image_64: typing.Optional[str] = Field(None, alias='image_64')
    class Config:
        arbitrary_types_allowed = True
