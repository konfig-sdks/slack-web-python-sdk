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

from slack_web_python_sdk.pydantic.appspermissionsresources_get_resources_list_response_resources import AppspermissionsresourcesGetResourcesListResponseResources
from slack_web_python_sdk.pydantic.appspermissionsresources_get_resources_list_response_response_metadata import AppspermissionsresourcesGetResourcesListResponseResponseMetadata
from slack_web_python_sdk.pydantic.defs_ok_true import DefsOkTrue

class AppspermissionsresourcesGetResourcesListResponse(BaseModel):
    ok: DefsOkTrue = Field(alias='ok')

    resources: AppspermissionsresourcesGetResourcesListResponseResources = Field(alias='resources')

    response_metadata: typing.Optional[AppspermissionsresourcesGetResourcesListResponseResponseMetadata] = Field(None, alias='response_metadata')
    class Config:
        arbitrary_types_allowed = True
