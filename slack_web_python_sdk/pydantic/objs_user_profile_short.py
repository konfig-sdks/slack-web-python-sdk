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

from slack_web_python_sdk.pydantic.defs_workspace_id import DefsWorkspaceId

class ObjsUserProfileShort(BaseModel):
    avatar_hash: str = Field(alias='avatar_hash')

    display_name: str = Field(alias='display_name')

    first_name: typing.Optional[str] = Field(alias='first_name')

    image_72: str = Field(alias='image_72')

    is_restricted: bool = Field(alias='is_restricted')

    is_ultra_restricted: bool = Field(alias='is_ultra_restricted')

    name: str = Field(alias='name')

    real_name: str = Field(alias='real_name')

    team: DefsWorkspaceId = Field(alias='team')

    display_name_normalized: typing.Optional[str] = Field(None, alias='display_name_normalized')

    real_name_normalized: typing.Optional[str] = Field(None, alias='real_name_normalized')
    class Config:
        arbitrary_types_allowed = True
