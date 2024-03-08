# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

from slack_web_python_sdk.paths.admin_emoji_add.post import AddEmojiRaw
from slack_web_python_sdk.paths.admin_emoji_add_alias.post import AliasAddRaw
from slack_web_python_sdk.paths.admin_emoji_list.get import ListEnterpriseEmojiRaw
from slack_web_python_sdk.paths.admin_emoji_remove.post import RemoveEnterpriseEmojiRaw
from slack_web_python_sdk.paths.admin_emoji_rename.post import RenameEmojiRaw


class AdminEmojiApiRaw(
    AddEmojiRaw,
    AliasAddRaw,
    ListEnterpriseEmojiRaw,
    RemoveEnterpriseEmojiRaw,
    RenameEmojiRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass