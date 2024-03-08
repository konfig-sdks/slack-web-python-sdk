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

from slack_web_python_sdk.pydantic.objs_team_profile_field_option import ObjsTeamProfileFieldOption
from slack_web_python_sdk.pydantic.objs_team_profile_field_possible_values import ObjsTeamProfileFieldPossibleValues

class ObjsTeamProfileField(BaseModel):
    hint: str = Field(alias='hint')

    id: str = Field(alias='id')

    label: str = Field(alias='label')

    ordering: typing.Union[int, float] = Field(alias='ordering')

    type: Literal["text", "date", "link", "mailto", "options_list", "user"] = Field(alias='type')

    field_name: typing.Optional[typing.Optional[str]] = Field(None, alias='field_name')

    is_hidden: typing.Optional[bool] = Field(None, alias='is_hidden')

    options: typing.Optional[typing.List[typing.Union[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[ObjsTeamProfileFieldOption]]]] = Field(None, alias='options')

    possible_values: typing.Optional[ObjsTeamProfileFieldPossibleValues] = Field(None, alias='possible_values')
    class Config:
        arbitrary_types_allowed = True
