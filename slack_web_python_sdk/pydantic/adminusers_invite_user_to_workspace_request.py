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


class AdminusersInviteUserToWorkspaceRequest(BaseModel):
    # A comma-separated list of `channel_id`s for this user to join. At least one channel is required.
    channel_ids: str = Field(alias='channel_ids')

    # The email address of the person to invite.
    email: str = Field(alias='email')

    # The ID (`T1234`) of the workspace.
    team_id: str = Field(alias='team_id')

    # An optional message to send to the user in the invite email.
    custom_message: typing.Optional[str] = Field(None, alias='custom_message')

    # Timestamp when guest account should be disabled. Only include this timestamp if you are inviting a guest user and you want their account to expire on a certain date.
    guest_expiration_ts: typing.Optional[str] = Field(None, alias='guest_expiration_ts')

    # Is this user a multi-channel guest user? (default: false)
    is_restricted: typing.Optional[bool] = Field(None, alias='is_restricted')

    # Is this user a single channel guest user? (default: false)
    is_ultra_restricted: typing.Optional[bool] = Field(None, alias='is_ultra_restricted')

    # Full name of the user.
    real_name: typing.Optional[str] = Field(None, alias='real_name')

    # Allow this invite to be resent in the future if a user has not signed up yet. (default: false)
    resend: typing.Optional[bool] = Field(None, alias='resend')
    class Config:
        arbitrary_types_allowed = True
