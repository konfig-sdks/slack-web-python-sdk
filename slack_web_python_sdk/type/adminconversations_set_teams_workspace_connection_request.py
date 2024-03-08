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


class RequiredAdminconversationsSetTeamsWorkspaceConnectionRequest(TypedDict):
    # The encoded `channel_id` to add or remove to workspaces.
    channel_id: str

class OptionalAdminconversationsSetTeamsWorkspaceConnectionRequest(TypedDict, total=False):
    # True if channel has to be converted to an org channel
    org_channel: bool

    # A comma-separated list of workspaces to which the channel should be shared. Not required if the channel is being shared org-wide.
    target_team_ids: str

    # The workspace to which the channel belongs. Omit this argument if the channel is a cross-workspace shared channel.
    team_id: str

class AdminconversationsSetTeamsWorkspaceConnectionRequest(RequiredAdminconversationsSetTeamsWorkspaceConnectionRequest, OptionalAdminconversationsSetTeamsWorkspaceConnectionRequest):
    pass
