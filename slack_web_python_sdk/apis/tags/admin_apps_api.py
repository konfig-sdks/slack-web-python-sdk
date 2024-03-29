# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

from slack_web_python_sdk.paths.admin_apps_approve.post import ApproveAppInstallation
from slack_web_python_sdk.paths.admin_apps_restrict.post import RestrictApp
from slack_web_python_sdk.apis.tags.admin_apps_api_raw import AdminAppsApiRaw


class AdminAppsApi(
    ApproveAppInstallation,
    RestrictApp,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AdminAppsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AdminAppsApiRaw(api_client)
