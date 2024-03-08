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
from slack_web_python_sdk.pydantic.defs_user_id import DefsUserId
from slack_web_python_sdk.pydantic.objs_comments import ObjsComments
from slack_web_python_sdk.pydantic.objs_file import ObjsFile
from slack_web_python_sdk.pydantic.objs_paging import ObjsPaging
from slack_web_python_sdk.pydantic.objs_response_metadata import ObjsResponseMetadata

class FilesInfoResponse(BaseModel):
    comments: ObjsComments = Field(alias='comments')

    file: ObjsFile = Field(alias='file')

    ok: DefsOkTrue = Field(alias='ok')

    content_html: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='content_html')

    editor: typing.Optional[DefsUserId] = Field(None, alias='editor')

    paging: typing.Optional[ObjsPaging] = Field(None, alias='paging')

    response_metadata: typing.Optional[ObjsResponseMetadata] = Field(None, alias='response_metadata')
    class Config:
        arbitrary_types_allowed = True
