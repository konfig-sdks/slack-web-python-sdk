# coding: utf-8

# flake8: noqa

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

__version__ = "1.7.0"

# import ApiClient
from slack_web_python_sdk.api_client import ApiClient

# import Configuration
from slack_web_python_sdk.configuration import Configuration

# import exceptions
from slack_web_python_sdk.exceptions import OpenApiException
from slack_web_python_sdk.exceptions import ApiAttributeError
from slack_web_python_sdk.exceptions import ApiTypeError
from slack_web_python_sdk.exceptions import ApiValueError
from slack_web_python_sdk.exceptions import ApiKeyError
from slack_web_python_sdk.exceptions import ApiException

from slack_web_python_sdk.client import SlackWeb
