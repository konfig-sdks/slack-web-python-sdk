# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

from slack_web_python_sdk.paths.pins_add.post import Add
from slack_web_python_sdk.paths.pins_list.get import List
from slack_web_python_sdk.paths.pins_remove.post import Remove
from slack_web_python_sdk.apis.tags.pins_api_raw import PinsApiRaw


class PinsApi(
    Add,
    List,
    Remove,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PinsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PinsApiRaw(api_client)
