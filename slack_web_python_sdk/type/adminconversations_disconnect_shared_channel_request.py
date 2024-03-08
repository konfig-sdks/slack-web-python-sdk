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


class RequiredAdminconversationsDisconnectSharedChannelRequest(TypedDict):
    # The channel to be disconnected from some workspaces.
    channel_id: str

class OptionalAdminconversationsDisconnectSharedChannelRequest(TypedDict, total=False):
    # The team to be removed from the channel. Currently only a single team id can be specified.
    leaving_team_ids: str

class AdminconversationsDisconnectSharedChannelRequest(RequiredAdminconversationsDisconnectSharedChannelRequest, OptionalAdminconversationsDisconnectSharedChannelRequest):
    pass
