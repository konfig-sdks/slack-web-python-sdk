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
from slack_web_python_sdk.type.defs_user_id import DefsUserId
from slack_web_python_sdk.type.objs_comments import ObjsComments
from slack_web_python_sdk.type.objs_file import ObjsFile
from slack_web_python_sdk.type.objs_paging import ObjsPaging
from slack_web_python_sdk.type.objs_response_metadata import ObjsResponseMetadata

class RequiredFilesInfoResponse(TypedDict):
    comments: ObjsComments

    file: ObjsFile

    ok: DefsOkTrue

class OptionalFilesInfoResponse(TypedDict, total=False):
    content_html: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    editor: DefsUserId

    paging: ObjsPaging

    response_metadata: ObjsResponseMetadata

class FilesInfoResponse(RequiredFilesInfoResponse, OptionalFilesInfoResponse):
    pass
