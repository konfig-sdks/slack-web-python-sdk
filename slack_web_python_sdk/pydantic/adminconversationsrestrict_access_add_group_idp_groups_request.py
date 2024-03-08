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


class AdminconversationsrestrictAccessAddGroupIdpGroupsRequest(BaseModel):
    # The channel to link this group to.
    channel_id: str = Field(alias='channel_id')

    # The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID to be an allowlist for the private channel.
    group_id: str = Field(alias='group_id')

    # Authentication token. Requires scope: `admin.conversations:write`
    token: str = Field(alias='token')

    # The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.
    team_id: typing.Optional[str] = Field(None, alias='team_id')
    class Config:
        arbitrary_types_allowed = True
