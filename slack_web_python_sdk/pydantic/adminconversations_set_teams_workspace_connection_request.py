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


class AdminconversationsSetTeamsWorkspaceConnectionRequest(BaseModel):
    # The encoded `channel_id` to add or remove to workspaces.
    channel_id: str = Field(alias='channel_id')

    # True if channel has to be converted to an org channel
    org_channel: typing.Optional[bool] = Field(None, alias='org_channel')

    # A comma-separated list of workspaces to which the channel should be shared. Not required if the channel is being shared org-wide.
    target_team_ids: typing.Optional[str] = Field(None, alias='target_team_ids')

    # The workspace to which the channel belongs. Omit this argument if the channel is a cross-workspace shared channel.
    team_id: typing.Optional[str] = Field(None, alias='team_id')
    class Config:
        arbitrary_types_allowed = True
