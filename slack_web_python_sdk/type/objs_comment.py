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

from slack_web_python_sdk.type.defs_channel import DefsChannel
from slack_web_python_sdk.type.defs_comment_id import DefsCommentId
from slack_web_python_sdk.type.defs_user_id import DefsUserId
from slack_web_python_sdk.type.objs_reaction import ObjsReaction

class RequiredObjsComment(TypedDict):
    comment: str

    created: int

    id: DefsCommentId

    is_intro: bool

    timestamp: int

    user: DefsUserId

class OptionalObjsComment(TypedDict, total=False):
    is_starred: bool

    num_stars: int

    pinned_info: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    pinned_to: typing.List[DefsChannel]

    reactions: typing.List[ObjsReaction]

class ObjsComment(RequiredObjsComment, OptionalObjsComment):
    pass
