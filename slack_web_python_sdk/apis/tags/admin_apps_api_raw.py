# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

from slack_web_python_sdk.paths.admin_apps_approve.post import ApproveAppInstallationRaw
from slack_web_python_sdk.paths.admin_apps_restrict.post import RestrictAppRaw


class AdminAppsApiRaw(
    ApproveAppInstallationRaw,
    RestrictAppRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
