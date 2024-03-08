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


class RequiredAdminusergroupsAssociateDefaultWorkspacesRequest(TypedDict):
    # A comma separated list of encoded team (workspace) IDs. Each workspace *MUST* belong to the organization associated with the token.
    team_ids: str

    # An encoded usergroup (IDP Group) ID.
    usergroup_id: str

class OptionalAdminusergroupsAssociateDefaultWorkspacesRequest(TypedDict, total=False):
    # When `true`, this method automatically creates new workspace accounts for the IDP group members.
    auto_provision: bool

class AdminusergroupsAssociateDefaultWorkspacesRequest(RequiredAdminusergroupsAssociateDefaultWorkspacesRequest, OptionalAdminusergroupsAssociateDefaultWorkspacesRequest):
    pass
