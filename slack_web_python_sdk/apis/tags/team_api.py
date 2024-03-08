# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

from slack_web_python_sdk.paths.team_access_logs.get import AccessLogs
from slack_web_python_sdk.paths.team_billable_info.get import BillableInfo
from slack_web_python_sdk.paths.team_profile_get.get import GetProfile
from slack_web_python_sdk.paths.team_info.get import Info
from slack_web_python_sdk.paths.team_integration_logs.get import IntegrationLogs
from slack_web_python_sdk.apis.tags.team_api_raw import TeamApiRaw


class TeamApi(
    AccessLogs,
    BillableInfo,
    GetProfile,
    Info,
    IntegrationLogs,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TeamApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TeamApiRaw(api_client)
