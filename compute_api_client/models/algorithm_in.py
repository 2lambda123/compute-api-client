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


class AlgorithmIn(object):
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
        'type': 'AlgorithmType',
        'shared': 'ShareType',
        'link': 'str',
        'project_id': 'int'
    }

    attribute_map = {
        'type': 'type',
        'shared': 'shared',
        'link': 'link',
        'project_id': 'project_id'
    }

    def __init__(self, type=None, shared=None, link=None, project_id=None, local_vars_configuration=None):  # noqa: E501
        """AlgorithmIn - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._shared = None
        self._link = None
        self._project_id = None
        self.discriminator = None

        self.type = type
        self.shared = shared
        self.link = link
        self.project_id = project_id

    @property
    def type(self):
        """Gets the type of this AlgorithmIn.  # noqa: E501

        HYBRID: hybrid<br/>QUANTUM: quantum  # noqa: E501

        :return: The type of this AlgorithmIn.  # noqa: E501
        :rtype: AlgorithmType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AlgorithmIn.

        HYBRID: hybrid<br/>QUANTUM: quantum  # noqa: E501

        :param type: The type of this AlgorithmIn.  # noqa: E501
        :type type: AlgorithmType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) > 7):
            raise ValueError("Invalid value for `type`, length must be less than or equal to `7`")  # noqa: E501

        self._type = type

    @property
    def shared(self):
        """Gets the shared of this AlgorithmIn.  # noqa: E501

        PRIVATE: private<br/>LINK_ONLY: link_only<br/>TEAM: team  # noqa: E501

        :return: The shared of this AlgorithmIn.  # noqa: E501
        :rtype: ShareType
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this AlgorithmIn.

        PRIVATE: private<br/>LINK_ONLY: link_only<br/>TEAM: team  # noqa: E501

        :param shared: The shared of this AlgorithmIn.  # noqa: E501
        :type shared: ShareType
        """
        if self.local_vars_configuration.client_side_validation and shared is None:  # noqa: E501
            raise ValueError("Invalid value for `shared`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                shared is not None and len(shared) > 9):
            raise ValueError("Invalid value for `shared`, length must be less than or equal to `9`")  # noqa: E501

        self._shared = shared

    @property
    def link(self):
        """Gets the link of this AlgorithmIn.  # noqa: E501


        :return: The link of this AlgorithmIn.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this AlgorithmIn.


        :param link: The link of this AlgorithmIn.  # noqa: E501
        :type link: str
        """
        if (self.local_vars_configuration.client_side_validation and
                link is not None and len(link) > 255):
            raise ValueError("Invalid value for `link`, length must be less than or equal to `255`")  # noqa: E501

        self._link = link

    @property
    def project_id(self):
        """Gets the project_id of this AlgorithmIn.  # noqa: E501


        :return: The project_id of this AlgorithmIn.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AlgorithmIn.


        :param project_id: The project_id of this AlgorithmIn.  # noqa: E501
        :type project_id: int
        """
        if self.local_vars_configuration.client_side_validation and project_id is None:  # noqa: E501
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                project_id is not None and project_id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `project_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                project_id is not None and project_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `project_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._project_id = project_id

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
        if not isinstance(other, AlgorithmIn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlgorithmIn):
            return True

        return self.to_dict() != other.to_dict()
