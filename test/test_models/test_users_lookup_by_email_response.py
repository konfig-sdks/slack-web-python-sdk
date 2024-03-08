# coding: utf-8

"""
    Slack Web API

    One way to interact with the Slack platform is its HTTP RPC-based Web API, a collection of methods requiring OAuth 2.0-based user, bot, or workspace tokens blessed with related OAuth scopes.

    The version of the OpenAPI document: 1.7.0
    Created by: https://api.slack.com/support
"""

import unittest

import slack_web_python_sdk
from slack_web_python_sdk.model.users_lookup_by_email_response import UsersLookupByEmailResponse
from slack_web_python_sdk import configuration


class TestUsersLookupByEmailResponse(unittest.TestCase):
    """UsersLookupByEmailResponse unit test stubs"""
    pass


if __name__ == '__main__':
    unittest.main()
