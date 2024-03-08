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

from slack_web_python_sdk.pydantic.defs_enterprise_id import DefsEnterpriseId
from slack_web_python_sdk.pydantic.defs_enterprise_user_id import DefsEnterpriseUserId
from slack_web_python_sdk.pydantic.defs_team import DefsTeam

class ObjsEnterpriseUser(BaseModel):
    enterprise_id: DefsEnterpriseId = Field(alias='enterprise_id')

    enterprise_name: str = Field(alias='enterprise_name')

    id: DefsEnterpriseUserId = Field(alias='id')

    is_admin: bool = Field(alias='is_admin')

    is_owner: bool = Field(alias='is_owner')

    teams: typing.List[DefsTeam] = Field(alias='teams')
    class Config:
        arbitrary_types_allowed = True
