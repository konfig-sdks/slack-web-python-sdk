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


class AdminusergroupsAddDefaultChannelsRequest(BaseModel):
    # Comma separated string of channel IDs.
    channel_ids: str = Field(alias='channel_ids')

    # ID of the IDP group to add default channels for.
    usergroup_id: str = Field(alias='usergroup_id')

    # The workspace to add default channels in.
    team_id: typing.Optional[str] = Field(None, alias='team_id')
    class Config:
        arbitrary_types_allowed = True
