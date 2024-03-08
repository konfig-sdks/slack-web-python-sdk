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


class UsersSetPhotoRequest(BaseModel):
    # Authentication token. Requires scope: `users.profile:write`
    token: str = Field(alias='token')

    # Width/height of crop box (always square)
    crop_w: typing.Optional[str] = Field(None, alias='crop_w')

    # X coordinate of top-left corner of crop box
    crop_x: typing.Optional[str] = Field(None, alias='crop_x')

    # Y coordinate of top-left corner of crop box
    crop_y: typing.Optional[str] = Field(None, alias='crop_y')

    # File contents via `multipart/form-data`.
    image: typing.Optional[str] = Field(None, alias='image')
    class Config:
        arbitrary_types_allowed = True
