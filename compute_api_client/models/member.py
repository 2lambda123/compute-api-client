# coding: utf-8

"""
    Quantum Inspire 2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from compute_api_client.configuration import Configuration


class Member(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'team_id': 'int',
        'user_id': 'int',
        'role': 'Role',
        'is_active': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'team_id': 'team_id',
        'user_id': 'user_id',
        'role': 'role',
        'is_active': 'is_active'
    }

    def __init__(self, id=None, team_id=None, user_id=None, role=None, is_active=None, local_vars_configuration=None):  # noqa: E501
        """Member - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._team_id = None
        self._user_id = None
        self._role = None
        self._is_active = None
        self.discriminator = None

        self.id = id
        self.team_id = team_id
        self.user_id = user_id
        self.role = role
        self.is_active = is_active

    @property
    def id(self):
        """Gets the id of this Member.  # noqa: E501


        :return: The id of this Member.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Member.


        :param id: The id of this Member.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def team_id(self):
        """Gets the team_id of this Member.  # noqa: E501


        :return: The team_id of this Member.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this Member.


        :param team_id: The team_id of this Member.  # noqa: E501
        :type team_id: int
        """
        if self.local_vars_configuration.client_side_validation and team_id is None:  # noqa: E501
            raise ValueError("Invalid value for `team_id`, must not be `None`")  # noqa: E501

        self._team_id = team_id

    @property
    def user_id(self):
        """Gets the user_id of this Member.  # noqa: E501


        :return: The user_id of this Member.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Member.


        :param user_id: The user_id of this Member.  # noqa: E501
        :type user_id: int
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def role(self):
        """Gets the role of this Member.  # noqa: E501


        :return: The role of this Member.  # noqa: E501
        :rtype: Role
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Member.


        :param role: The role of this Member.  # noqa: E501
        :type role: Role
        """
        if self.local_vars_configuration.client_side_validation and role is None:  # noqa: E501
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def is_active(self):
        """Gets the is_active of this Member.  # noqa: E501


        :return: The is_active of this Member.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this Member.


        :param is_active: The is_active of this Member.  # noqa: E501
        :type is_active: bool
        """
        if self.local_vars_configuration.client_side_validation and is_active is None:  # noqa: E501
            raise ValueError("Invalid value for `is_active`, must not be `None`")  # noqa: E501

        self._is_active = is_active

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Member):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Member):
            return True

        return self.to_dict() != other.to_dict()
