# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

import unittest

import os
from pprint import pprint
from slack_web_python_sdk import SlackWeb

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        slackweb = SlackWeb(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(slackweb)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
