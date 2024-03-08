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


class AdminemojiRemoveEnterpriseEmojiRequest(BaseModel):
    # The name of the emoji to be removed. Colons (`:myemoji:`) around the value are not required, although they may be included.
    name: str = Field(alias='name')

    # Authentication token. Requires scope: `admin.teams:write`
    token: str = Field(alias='token')
    class Config:
        arbitrary_types_allowed = True
