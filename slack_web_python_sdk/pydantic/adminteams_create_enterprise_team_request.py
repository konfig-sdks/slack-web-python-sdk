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


class AdminteamsCreateEnterpriseTeamRequest(BaseModel):
    # Team domain (for example, slacksoftballteam).
    team_domain: str = Field(alias='team_domain')

    # Team name (for example, Slack Softball Team).
    team_name: str = Field(alias='team_name')

    # Description for the team.
    team_description: typing.Optional[str] = Field(None, alias='team_description')

    # Who can join the team. A team's discoverability can be `open`, `closed`, `invite_only`, or `unlisted`.
    team_discoverability: typing.Optional[str] = Field(None, alias='team_discoverability')
    class Config:
        arbitrary_types_allowed = True
