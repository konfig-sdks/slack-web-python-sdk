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

from slack_web_python_sdk.pydantic.appspermissions_list_permissions_response_info_app_home import AppspermissionsListPermissionsResponseInfoAppHome
from slack_web_python_sdk.pydantic.appspermissions_list_permissions_response_info_channel import AppspermissionsListPermissionsResponseInfoChannel
from slack_web_python_sdk.pydantic.appspermissions_list_permissions_response_info_group import AppspermissionsListPermissionsResponseInfoGroup
from slack_web_python_sdk.pydantic.appspermissions_list_permissions_response_info_im import AppspermissionsListPermissionsResponseInfoIm
from slack_web_python_sdk.pydantic.appspermissions_list_permissions_response_info_mpim import AppspermissionsListPermissionsResponseInfoMpim
from slack_web_python_sdk.pydantic.appspermissions_list_permissions_response_info_team import AppspermissionsListPermissionsResponseInfoTeam

class AppspermissionsListPermissionsResponseInfo(BaseModel):
    app_home: AppspermissionsListPermissionsResponseInfoAppHome = Field(alias='app_home')

    channel: AppspermissionsListPermissionsResponseInfoChannel = Field(alias='channel')

    group: AppspermissionsListPermissionsResponseInfoGroup = Field(alias='group')

    im: AppspermissionsListPermissionsResponseInfoIm = Field(alias='im')

    mpim: AppspermissionsListPermissionsResponseInfoMpim = Field(alias='mpim')

    team: AppspermissionsListPermissionsResponseInfoTeam = Field(alias='team')
    class Config:
        arbitrary_types_allowed = True
