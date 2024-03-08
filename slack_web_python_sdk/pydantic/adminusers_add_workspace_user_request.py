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


class AdminusersAddWorkspaceUserRequest(BaseModel):
    # The ID (`T1234`) of the workspace.
    team_id: str = Field(alias='team_id')

    # The ID of the user to add to the workspace.
    user_id: str = Field(alias='user_id')

    # Comma separated values of channel IDs to add user in the new workspace.
    channel_ids: typing.Optional[str] = Field(None, alias='channel_ids')

    # True if user should be added to the workspace as a guest.
    is_restricted: typing.Optional[bool] = Field(None, alias='is_restricted')

    # True if user should be added to the workspace as a single-channel guest.
    is_ultra_restricted: typing.Optional[bool] = Field(None, alias='is_ultra_restricted')
    class Config:
        arbitrary_types_allowed = True
