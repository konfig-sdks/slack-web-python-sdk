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


class ChatUnfurlRequest(BaseModel):
    # Channel ID of the message
    channel: str = Field(alias='channel')

    # Timestamp of the message to add unfurl behavior to.
    ts: str = Field(alias='ts')

    # URL-encoded JSON map with keys set to URLs featured in the the message, pointing to their unfurl blocks or message attachments.
    unfurls: typing.Optional[str] = Field(None, alias='unfurls')

    # Provide a simply-formatted string to send as an ephemeral message to the user as invitation to authenticate further and enable full unfurling behavior
    user_auth_message: typing.Optional[str] = Field(None, alias='user_auth_message')

    # Set to `true` or `1` to indicate the user must install your Slack app to trigger unfurls for this domain
    user_auth_required: typing.Optional[bool] = Field(None, alias='user_auth_required')

    # Send users to this custom URL where they will complete authentication in your app to fully trigger unfurling. Value should be properly URL-encoded.
    user_auth_url: typing.Optional[str] = Field(None, alias='user_auth_url')
    class Config:
        arbitrary_types_allowed = True
