# coding: utf-8

"""
    Quantum Inspire 2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import compute_api_client
from compute_api_client.api.members_api import MembersApi  # noqa: E501
from compute_api_client.rest import ApiException


class TestMembersApi(unittest.TestCase):
    """MembersApi unit test stubs"""

    def setUp(self):
        self.api = compute_api_client.api.members_api.MembersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_member_members_post(self):
        """Test case for create_member_members_post

        Create member  # noqa: E501
        """
        pass

    def test_delete_member_members_id_delete(self):
        """Test case for delete_member_members_id_delete

        Destroy member  # noqa: E501
        """
        pass

    def test_read_member_members_id_get(self):
        """Test case for read_member_members_id_get

        Retrieve member  # noqa: E501
        """
        pass

    def test_read_members_members_get(self):
        """Test case for read_members_members_get

        List members  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
