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


class UsersSetPhotoResponseProfile(BaseModel):
    avatar_hash: str = Field(alias='avatar_hash')

    image_1024: str = Field(alias='image_1024')

    image_192: str = Field(alias='image_192')

    image_24: str = Field(alias='image_24')

    image_32: str = Field(alias='image_32')

    image_48: str = Field(alias='image_48')

    image_512: str = Field(alias='image_512')

    image_72: str = Field(alias='image_72')

    image_original: str = Field(alias='image_original')
    class Config:
        arbitrary_types_allowed = True
