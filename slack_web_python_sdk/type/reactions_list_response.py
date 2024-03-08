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
from slack_web_python_sdk.type.objs_paging import ObjsPaging
from slack_web_python_sdk.type.objs_response_metadata import ObjsResponseMetadata
from slack_web_python_sdk.type.reactions_list_response_items import ReactionsListResponseItems

class RequiredReactionsListResponse(TypedDict):
    items: ReactionsListResponseItems

    ok: DefsOkTrue

class OptionalReactionsListResponse(TypedDict, total=False):
    paging: ObjsPaging

    response_metadata: ObjsResponseMetadata

class ReactionsListResponse(RequiredReactionsListResponse, OptionalReactionsListResponse):
    pass
