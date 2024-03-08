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

from slack_web_python_sdk.type.defs_ok_true import DefsOkTrue
from slack_web_python_sdk.type.defs_team import DefsTeam
from slack_web_python_sdk.type.migration_exchange_response_invalid_user_ids import MigrationExchangeResponseInvalidUserIds
from slack_web_python_sdk.type.migration_exchange_response_user_id_map import MigrationExchangeResponseUserIdMap

class RequiredMigrationExchangeResponse(TypedDict):
    enterprise_id: str

    ok: DefsOkTrue

    team_id: DefsTeam

class OptionalMigrationExchangeResponse(TypedDict, total=False):
    invalid_user_ids: MigrationExchangeResponseInvalidUserIds

    user_id_map: MigrationExchangeResponseUserIdMap

class MigrationExchangeResponse(RequiredMigrationExchangeResponse, OptionalMigrationExchangeResponse):
    pass
