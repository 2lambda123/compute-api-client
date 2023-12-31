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


class ReservationIn(object):
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
        'member_id': 'int',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'backend_type_id': 'int'
    }

    attribute_map = {
        'member_id': 'member_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'backend_type_id': 'backend_type_id'
    }

    def __init__(self, member_id=None, start_time=None, end_time=None, backend_type_id=None, local_vars_configuration=None):  # noqa: E501
        """ReservationIn - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._member_id = None
        self._start_time = None
        self._end_time = None
        self._backend_type_id = None
        self.discriminator = None

        self.member_id = member_id
        self.start_time = start_time
        self.end_time = end_time
        self.backend_type_id = backend_type_id

    @property
    def member_id(self):
        """Gets the member_id of this ReservationIn.  # noqa: E501


        :return: The member_id of this ReservationIn.  # noqa: E501
        :rtype: int
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """Sets the member_id of this ReservationIn.


        :param member_id: The member_id of this ReservationIn.  # noqa: E501
        :type member_id: int
        """
        if self.local_vars_configuration.client_side_validation and member_id is None:  # noqa: E501
            raise ValueError("Invalid value for `member_id`, must not be `None`")  # noqa: E501

        self._member_id = member_id

    @property
    def start_time(self):
        """Gets the start_time of this ReservationIn.  # noqa: E501


        :return: The start_time of this ReservationIn.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ReservationIn.


        :param start_time: The start_time of this ReservationIn.  # noqa: E501
        :type start_time: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_time is None:  # noqa: E501
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ReservationIn.  # noqa: E501


        :return: The end_time of this ReservationIn.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ReservationIn.


        :param end_time: The end_time of this ReservationIn.  # noqa: E501
        :type end_time: datetime
        """
        if self.local_vars_configuration.client_side_validation and end_time is None:  # noqa: E501
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def backend_type_id(self):
        """Gets the backend_type_id of this ReservationIn.  # noqa: E501


        :return: The backend_type_id of this ReservationIn.  # noqa: E501
        :rtype: int
        """
        return self._backend_type_id

    @backend_type_id.setter
    def backend_type_id(self, backend_type_id):
        """Sets the backend_type_id of this ReservationIn.


        :param backend_type_id: The backend_type_id of this ReservationIn.  # noqa: E501
        :type backend_type_id: int
        """
        if self.local_vars_configuration.client_side_validation and backend_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `backend_type_id`, must not be `None`")  # noqa: E501

        self._backend_type_id = backend_type_id

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
        if not isinstance(other, ReservationIn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReservationIn):
            return True

        return self.to_dict() != other.to_dict()
