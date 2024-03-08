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


class RequiredAdminusersAddWorkspaceUserRequest(TypedDict):
    # The ID (`T1234`) of the workspace.
    team_id: str

    # The ID of the user to add to the workspace.
    user_id: str

class OptionalAdminusersAddWorkspaceUserRequest(TypedDict, total=False):
    # Comma separated values of channel IDs to add user in the new workspace.
    channel_ids: str

    # True if user should be added to the workspace as a guest.
    is_restricted: bool

    # True if user should be added to the workspace as a single-channel guest.
    is_ultra_restricted: bool

class AdminusersAddWorkspaceUserRequest(RequiredAdminusersAddWorkspaceUserRequest, OptionalAdminusersAddWorkspaceUserRequest):
    pass
