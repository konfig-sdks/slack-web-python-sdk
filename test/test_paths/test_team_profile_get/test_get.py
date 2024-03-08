# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

import unittest
from unittest.mock import patch

import urllib3

import slack_web_python_sdk
from slack_web_python_sdk.paths.team_profile_get import get
from slack_web_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestTeamProfileGet(ApiTestMixin, unittest.TestCase):
    """
    TeamProfileGet unit test stubs
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()