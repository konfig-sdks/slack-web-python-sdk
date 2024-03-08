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

from slack_web_python_sdk.pydantic.defs_channel import DefsChannel
from slack_web_python_sdk.pydantic.defs_comment_id import DefsCommentId
from slack_web_python_sdk.pydantic.defs_user_id import DefsUserId
from slack_web_python_sdk.pydantic.objs_reaction import ObjsReaction

class ObjsComment(BaseModel):
    comment: str = Field(alias='comment')

    created: int = Field(alias='created')

    id: DefsCommentId = Field(alias='id')

    is_intro: bool = Field(alias='is_intro')

    timestamp: int = Field(alias='timestamp')

    user: DefsUserId = Field(alias='user')

    is_starred: typing.Optional[bool] = Field(None, alias='is_starred')

    num_stars: typing.Optional[int] = Field(None, alias='num_stars')

    pinned_info: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='pinned_info')

    pinned_to: typing.Optional[typing.List[DefsChannel]] = Field(None, alias='pinned_to')

    reactions: typing.Optional[typing.List[ObjsReaction]] = Field(None, alias='reactions')
    class Config:
        arbitrary_types_allowed = True
