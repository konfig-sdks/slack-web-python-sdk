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


class UsersprofileSetProfileInfoRequest(BaseModel):
    # Name of a single key to set. Usable only if `profile` is not passed.
    name: typing.Optional[str] = Field(None, alias='name')

    # Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may be set. Each field name is limited to 255 characters.
    profile: typing.Optional[str] = Field(None, alias='profile')

    # ID of user to change. This argument may only be specified by team admins on paid teams.
    user: typing.Optional[str] = Field(None, alias='user')

    # Value to set a single key to. Usable only if `profile` is not passed.
    value: typing.Optional[str] = Field(None, alias='value')
    class Config:
        arbitrary_types_allowed = True
