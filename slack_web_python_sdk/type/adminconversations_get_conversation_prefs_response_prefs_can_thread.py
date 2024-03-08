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

from slack_web_python_sdk.type.adminconversations_get_conversation_prefs_response_prefs_can_thread_type import AdminconversationsGetConversationPrefsResponsePrefsCanThreadType
from slack_web_python_sdk.type.adminconversations_get_conversation_prefs_response_prefs_can_thread_user import AdminconversationsGetConversationPrefsResponsePrefsCanThreadUser

class RequiredAdminconversationsGetConversationPrefsResponsePrefsCanThread(TypedDict):
    pass

class OptionalAdminconversationsGetConversationPrefsResponsePrefsCanThread(TypedDict, total=False):
    type: AdminconversationsGetConversationPrefsResponsePrefsCanThreadType

    user: AdminconversationsGetConversationPrefsResponsePrefsCanThreadUser

class AdminconversationsGetConversationPrefsResponsePrefsCanThread(RequiredAdminconversationsGetConversationPrefsResponsePrefsCanThread, OptionalAdminconversationsGetConversationPrefsResponsePrefsCanThread):
    pass
