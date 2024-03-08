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

from slack_web_python_sdk.pydantic.defs_ok_true import DefsOkTrue
from slack_web_python_sdk.pydantic.objs_paging import ObjsPaging
from slack_web_python_sdk.pydantic.team_access_logs_response_logins import TeamAccessLogsResponseLogins

class TeamAccessLogsResponse(BaseModel):
    logins: TeamAccessLogsResponseLogins = Field(alias='logins')

    ok: DefsOkTrue = Field(alias='ok')

    paging: ObjsPaging = Field(alias='paging')
    class Config:
        arbitrary_types_allowed = True
