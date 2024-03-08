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


class RequiredObjsIcon(TypedDict):
    pass

class OptionalObjsIcon(TypedDict, total=False):
    image_102: str

    image_132: str

    image_230: str

    image_34: str

    image_44: str

    image_68: str

    image_88: str

    image_default: bool

class ObjsIcon(RequiredObjsIcon, OptionalObjsIcon):
    pass
