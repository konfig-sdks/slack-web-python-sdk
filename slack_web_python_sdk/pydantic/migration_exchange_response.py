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
from slack_web_python_sdk.pydantic.defs_team import DefsTeam
from slack_web_python_sdk.pydantic.migration_exchange_response_invalid_user_ids import MigrationExchangeResponseInvalidUserIds
from slack_web_python_sdk.pydantic.migration_exchange_response_user_id_map import MigrationExchangeResponseUserIdMap

class MigrationExchangeResponse(BaseModel):
    enterprise_id: str = Field(alias='enterprise_id')

    ok: DefsOkTrue = Field(alias='ok')

    team_id: DefsTeam = Field(alias='team_id')

    invalid_user_ids: typing.Optional[MigrationExchangeResponseInvalidUserIds] = Field(None, alias='invalid_user_ids')

    user_id_map: typing.Optional[MigrationExchangeResponseUserIdMap] = Field(None, alias='user_id_map')
    class Config:
        arbitrary_types_allowed = True
