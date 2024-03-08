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

from slack_web_python_sdk.pydantic.defs_ok_false import DefsOkFalse
from slack_web_python_sdk.pydantic.defs_user_id import DefsUserId

class ConversationsInvitedefaultResponseErrorsItem(BaseModel):
    error: Literal["method_not_supported_for_channel_type", "missing_scope", "channel_not_found", "user_not_found", "no_user", "cant_invite_self", "not_in_channel", "already_in_channel", "is_archived", "cant_invite", "too_many_users", "ura_max_channels", "not_authed", "invalid_auth", "account_inactive", "user_is_bot", "user_is_restricted", "user_is_ultra_restricted", "invalid_arg_name", "invalid_array_arg", "invalid_charset", "invalid_form_data", "invalid_post_type", "missing_post_type", "invalid_json", "json_not_object", "request_timeout", "upgrade_required", "team_added_to_org", "missing_charset", "superfluous_charset"] = Field(alias='error')

    ok: DefsOkFalse = Field(alias='ok')

    user: typing.Optional[DefsUserId] = Field(None, alias='user')
    class Config:
        arbitrary_types_allowed = True
