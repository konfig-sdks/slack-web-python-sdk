# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

from slack_web_python_sdk.paths.team_access_logs.get import AccessLogsRaw
from slack_web_python_sdk.paths.team_billable_info.get import BillableInfoRaw
from slack_web_python_sdk.paths.team_profile_get.get import GetProfileRaw
from slack_web_python_sdk.paths.team_info.get import InfoRaw
from slack_web_python_sdk.paths.team_integration_logs.get import IntegrationLogsRaw


class TeamApiRaw(
    AccessLogsRaw,
    BillableInfoRaw,
    GetProfileRaw,
    InfoRaw,
    IntegrationLogsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
