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


class RequiredAdminusergroupsAddDefaultChannelsRequest(TypedDict):
    # Comma separated string of channel IDs.
    channel_ids: str

    # ID of the IDP group to add default channels for.
    usergroup_id: str

class OptionalAdminusergroupsAddDefaultChannelsRequest(TypedDict, total=False):
    # The workspace to add default channels in.
    team_id: str

class AdminusergroupsAddDefaultChannelsRequest(RequiredAdminusergroupsAddDefaultChannelsRequest, OptionalAdminusergroupsAddDefaultChannelsRequest):
    pass
