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


class UsergroupsUpdateRequest(BaseModel):
    # The encoded ID of the User Group to update.
    usergroup: str = Field(alias='usergroup')

    # A short description of the User Group.
    description: typing.Optional[str] = Field(None, alias='description')

    # A comma separated string of encoded channel IDs for which the User Group uses as a default.
    channels: typing.Optional[str] = Field(None, alias='channels')

    # A mention handle. Must be unique among channels, users and User Groups.
    handle: typing.Optional[str] = Field(None, alias='handle')

    # Include the number of users in the User Group.
    include_count: typing.Optional[bool] = Field(None, alias='include_count')

    # A name for the User Group. Must be unique among User Groups.
    name: typing.Optional[str] = Field(None, alias='name')
    class Config:
        arbitrary_types_allowed = True
