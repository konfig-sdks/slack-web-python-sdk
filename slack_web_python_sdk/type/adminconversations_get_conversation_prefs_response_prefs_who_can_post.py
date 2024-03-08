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

from slack_web_python_sdk.type.adminconversations_get_conversation_prefs_response_prefs_who_can_post_type import AdminconversationsGetConversationPrefsResponsePrefsWhoCanPostType
from slack_web_python_sdk.type.adminconversations_get_conversation_prefs_response_prefs_who_can_post_user import AdminconversationsGetConversationPrefsResponsePrefsWhoCanPostUser

class RequiredAdminconversationsGetConversationPrefsResponsePrefsWhoCanPost(TypedDict):
    pass

class OptionalAdminconversationsGetConversationPrefsResponsePrefsWhoCanPost(TypedDict, total=False):
    type: AdminconversationsGetConversationPrefsResponsePrefsWhoCanPostType

    user: AdminconversationsGetConversationPrefsResponsePrefsWhoCanPostUser

class AdminconversationsGetConversationPrefsResponsePrefsWhoCanPost(RequiredAdminconversationsGetConversationPrefsResponsePrefsWhoCanPost, OptionalAdminconversationsGetConversationPrefsResponsePrefsWhoCanPost):
    pass
