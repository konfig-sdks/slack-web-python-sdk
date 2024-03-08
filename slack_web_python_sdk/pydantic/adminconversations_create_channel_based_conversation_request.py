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


class AdminconversationsCreateChannelBasedConversationRequest(BaseModel):
    # When `true`, creates a private channel instead of a public channel
    is_private: bool = Field(alias='is_private')

    # Name of the public or private channel to create.
    name: str = Field(alias='name')

    # Description of the public or private channel to create.
    description: typing.Optional[str] = Field(None, alias='description')

    # When `true`, the channel will be available org-wide. Note: if the channel is not `org_wide=true`, you must specify a `team_id` for this channel
    org_wide: typing.Optional[bool] = Field(None, alias='org_wide')

    # The workspace to create the channel in. Note: this argument is required unless you set `org_wide=true`.
    team_id: typing.Optional[str] = Field(None, alias='team_id')
    class Config:
        arbitrary_types_allowed = True
