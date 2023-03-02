# coding: utf-8

"""
    Compute Job Manager

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


class ResultIn(object):
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
        'number_of_qubits': 'int',
        'execution_time_in_seconds': 'float',
        'shots_requested': 'int',
        'shots_done': 'int',
        'results': 'object',
        'metadata_id': 'int',
        'run_id': 'int'
    }

    attribute_map = {
        'number_of_qubits': 'number_of_qubits',
        'execution_time_in_seconds': 'execution_time_in_seconds',
        'shots_requested': 'shots_requested',
        'shots_done': 'shots_done',
        'results': 'results',
        'metadata_id': 'metadata_id',
        'run_id': 'run_id'
    }

    def __init__(self, number_of_qubits=None, execution_time_in_seconds=None, shots_requested=None, shots_done=None, results=None, metadata_id=None, run_id=None, local_vars_configuration=None):  # noqa: E501
        """ResultIn - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._number_of_qubits = None
        self._execution_time_in_seconds = None
        self._shots_requested = None
        self._shots_done = None
        self._results = None
        self._metadata_id = None
        self._run_id = None
        self.discriminator = None

        self.number_of_qubits = number_of_qubits
        self.execution_time_in_seconds = execution_time_in_seconds
        self.shots_requested = shots_requested
        self.shots_done = shots_done
        self.results = results
        self.metadata_id = metadata_id
        self.run_id = run_id

    @property
    def number_of_qubits(self):
        """Gets the number_of_qubits of this ResultIn.  # noqa: E501


        :return: The number_of_qubits of this ResultIn.  # noqa: E501
        :rtype: int
        """
        return self._number_of_qubits

    @number_of_qubits.setter
    def number_of_qubits(self, number_of_qubits):
        """Sets the number_of_qubits of this ResultIn.


        :param number_of_qubits: The number_of_qubits of this ResultIn.  # noqa: E501
        :type number_of_qubits: int
        """
        if self.local_vars_configuration.client_side_validation and number_of_qubits is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_qubits`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number_of_qubits is not None and number_of_qubits > 32767):  # noqa: E501
            raise ValueError("Invalid value for `number_of_qubits`, must be a value less than or equal to `32767`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number_of_qubits is not None and number_of_qubits < -32768):  # noqa: E501
            raise ValueError("Invalid value for `number_of_qubits`, must be a value greater than or equal to `-32768`")  # noqa: E501

        self._number_of_qubits = number_of_qubits

    @property
    def execution_time_in_seconds(self):
        """Gets the execution_time_in_seconds of this ResultIn.  # noqa: E501


        :return: The execution_time_in_seconds of this ResultIn.  # noqa: E501
        :rtype: float
        """
        return self._execution_time_in_seconds

    @execution_time_in_seconds.setter
    def execution_time_in_seconds(self, execution_time_in_seconds):
        """Sets the execution_time_in_seconds of this ResultIn.


        :param execution_time_in_seconds: The execution_time_in_seconds of this ResultIn.  # noqa: E501
        :type execution_time_in_seconds: float
        """
        if self.local_vars_configuration.client_side_validation and execution_time_in_seconds is None:  # noqa: E501
            raise ValueError("Invalid value for `execution_time_in_seconds`, must not be `None`")  # noqa: E501

        self._execution_time_in_seconds = execution_time_in_seconds

    @property
    def shots_requested(self):
        """Gets the shots_requested of this ResultIn.  # noqa: E501


        :return: The shots_requested of this ResultIn.  # noqa: E501
        :rtype: int
        """
        return self._shots_requested

    @shots_requested.setter
    def shots_requested(self, shots_requested):
        """Sets the shots_requested of this ResultIn.


        :param shots_requested: The shots_requested of this ResultIn.  # noqa: E501
        :type shots_requested: int
        """
        if (self.local_vars_configuration.client_side_validation and
                shots_requested is not None and shots_requested > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `shots_requested`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                shots_requested is not None and shots_requested < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `shots_requested`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._shots_requested = shots_requested

    @property
    def shots_done(self):
        """Gets the shots_done of this ResultIn.  # noqa: E501


        :return: The shots_done of this ResultIn.  # noqa: E501
        :rtype: int
        """
        return self._shots_done

    @shots_done.setter
    def shots_done(self, shots_done):
        """Sets the shots_done of this ResultIn.


        :param shots_done: The shots_done of this ResultIn.  # noqa: E501
        :type shots_done: int
        """
        if (self.local_vars_configuration.client_side_validation and
                shots_done is not None and shots_done > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `shots_done`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                shots_done is not None and shots_done < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `shots_done`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._shots_done = shots_done

    @property
    def results(self):
        """Gets the results of this ResultIn.  # noqa: E501


        :return: The results of this ResultIn.  # noqa: E501
        :rtype: object
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this ResultIn.


        :param results: The results of this ResultIn.  # noqa: E501
        :type results: object
        """

        self._results = results

    @property
    def metadata_id(self):
        """Gets the metadata_id of this ResultIn.  # noqa: E501


        :return: The metadata_id of this ResultIn.  # noqa: E501
        :rtype: int
        """
        return self._metadata_id

    @metadata_id.setter
    def metadata_id(self, metadata_id):
        """Sets the metadata_id of this ResultIn.


        :param metadata_id: The metadata_id of this ResultIn.  # noqa: E501
        :type metadata_id: int
        """
        if self.local_vars_configuration.client_side_validation and metadata_id is None:  # noqa: E501
            raise ValueError("Invalid value for `metadata_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                metadata_id is not None and metadata_id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `metadata_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                metadata_id is not None and metadata_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `metadata_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._metadata_id = metadata_id

    @property
    def run_id(self):
        """Gets the run_id of this ResultIn.  # noqa: E501


        :return: The run_id of this ResultIn.  # noqa: E501
        :rtype: int
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this ResultIn.


        :param run_id: The run_id of this ResultIn.  # noqa: E501
        :type run_id: int
        """
        if self.local_vars_configuration.client_side_validation and run_id is None:  # noqa: E501
            raise ValueError("Invalid value for `run_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                run_id is not None and run_id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `run_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                run_id is not None and run_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `run_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._run_id = run_id

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
        if not isinstance(other, ResultIn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResultIn):
            return True

        return self.to_dict() != other.to_dict()
