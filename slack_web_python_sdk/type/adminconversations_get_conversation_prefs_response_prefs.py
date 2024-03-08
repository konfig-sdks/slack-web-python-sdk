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

from slack_web_python_sdk.type.adminconversations_get_conversation_prefs_response_prefs_can_thread import AdminconversationsGetConversationPrefsResponsePrefsCanThread
from slack_web_python_sdk.type.adminconversations_get_conversation_prefs_response_prefs_who_can_post import AdminconversationsGetConversationPrefsResponsePrefsWhoCanPost

class RequiredAdminconversationsGetConversationPrefsResponsePrefs(TypedDict):
    pass

class OptionalAdminconversationsGetConversationPrefsResponsePrefs(TypedDict, total=False):
    can_thread: AdminconversationsGetConversationPrefsResponsePrefsCanThread

    who_can_post: AdminconversationsGetConversationPrefsResponsePrefsWhoCanPost

class AdminconversationsGetConversationPrefsResponsePrefs(RequiredAdminconversationsGetConversationPrefsResponsePrefs, OptionalAdminconversationsGetConversationPrefsResponsePrefs):
    pass
