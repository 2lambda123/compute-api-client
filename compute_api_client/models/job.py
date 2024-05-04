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


class Job(object):
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
        'created_on': 'datetime',
        'file_id': 'int',
        'algorithm_type': 'AlgorithmType',
        'status': 'JobStatus',
        'batch_job_id': 'int',
        'queued_at': 'datetime',
        'finished_at': 'datetime',
        'number_of_shots': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_on': 'created_on',
        'file_id': 'file_id',
        'algorithm_type': 'algorithm_type',
        'status': 'status',
        'batch_job_id': 'batch_job_id',
        'queued_at': 'queued_at',
        'finished_at': 'finished_at',
        'number_of_shots': 'number_of_shots'
    }

    def __init__(self, id=None, created_on=None, file_id=None, algorithm_type=None, status=None, batch_job_id=None, queued_at=None, finished_at=None, number_of_shots=None, local_vars_configuration=None):  # noqa: E501
        """Job - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_on = None
        self._file_id = None
        self._algorithm_type = None
        self._status = None
        self._batch_job_id = None
        self._queued_at = None
        self._finished_at = None
        self._number_of_shots = None
        self.discriminator = None

        self.id = id
        self.created_on = created_on
        self.file_id = file_id
        self.algorithm_type = algorithm_type
        self.status = status
        self.batch_job_id = batch_job_id
        if queued_at is not None:
            self.queued_at = queued_at
        if finished_at is not None:
            self.finished_at = finished_at
        if number_of_shots is not None:
            self.number_of_shots = number_of_shots

    @property
    def id(self):
        """Gets the id of this Job.  # noqa: E501


        :return: The id of this Job.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Job.


        :param id: The id of this Job.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_on(self):
        """Gets the created_on of this Job.  # noqa: E501


        :return: The created_on of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Job.


        :param created_on: The created_on of this Job.  # noqa: E501
        :type created_on: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_on is None:  # noqa: E501
            raise ValueError("Invalid value for `created_on`, must not be `None`")  # noqa: E501

        self._created_on = created_on

    @property
    def file_id(self):
        """Gets the file_id of this Job.  # noqa: E501


        :return: The file_id of this Job.  # noqa: E501
        :rtype: int
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this Job.


        :param file_id: The file_id of this Job.  # noqa: E501
        :type file_id: int
        """
        if self.local_vars_configuration.client_side_validation and file_id is None:  # noqa: E501
            raise ValueError("Invalid value for `file_id`, must not be `None`")  # noqa: E501

        self._file_id = file_id

    @property
    def algorithm_type(self):
        """Gets the algorithm_type of this Job.  # noqa: E501


        :return: The algorithm_type of this Job.  # noqa: E501
        :rtype: AlgorithmType
        """
        return self._algorithm_type

    @algorithm_type.setter
    def algorithm_type(self, algorithm_type):
        """Sets the algorithm_type of this Job.


        :param algorithm_type: The algorithm_type of this Job.  # noqa: E501
        :type algorithm_type: AlgorithmType
        """
        if self.local_vars_configuration.client_side_validation and algorithm_type is None:  # noqa: E501
            raise ValueError("Invalid value for `algorithm_type`, must not be `None`")  # noqa: E501

        self._algorithm_type = algorithm_type

    @property
    def status(self):
        """Gets the status of this Job.  # noqa: E501


        :return: The status of this Job.  # noqa: E501
        :rtype: JobStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Job.


        :param status: The status of this Job.  # noqa: E501
        :type status: JobStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def batch_job_id(self):
        """Gets the batch_job_id of this Job.  # noqa: E501


        :return: The batch_job_id of this Job.  # noqa: E501
        :rtype: int
        """
        return self._batch_job_id

    @batch_job_id.setter
    def batch_job_id(self, batch_job_id):
        """Sets the batch_job_id of this Job.


        :param batch_job_id: The batch_job_id of this Job.  # noqa: E501
        :type batch_job_id: int
        """
        if self.local_vars_configuration.client_side_validation and batch_job_id is None:  # noqa: E501
            raise ValueError("Invalid value for `batch_job_id`, must not be `None`")  # noqa: E501

        self._batch_job_id = batch_job_id

    @property
    def queued_at(self):
        """Gets the queued_at of this Job.  # noqa: E501


        :return: The queued_at of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._queued_at

    @queued_at.setter
    def queued_at(self, queued_at):
        """Sets the queued_at of this Job.


        :param queued_at: The queued_at of this Job.  # noqa: E501
        :type queued_at: datetime
        """

        self._queued_at = queued_at

    @property
    def finished_at(self):
        """Gets the finished_at of this Job.  # noqa: E501


        :return: The finished_at of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this Job.


        :param finished_at: The finished_at of this Job.  # noqa: E501
        :type finished_at: datetime
        """

        self._finished_at = finished_at

    @property
    def number_of_shots(self):
        """Gets the number_of_shots of this Job.  # noqa: E501


        :return: The number_of_shots of this Job.  # noqa: E501
        :rtype: int
        """
        return self._number_of_shots

    @number_of_shots.setter
    def number_of_shots(self, number_of_shots):
        """Sets the number_of_shots of this Job.


        :param number_of_shots: The number_of_shots of this Job.  # noqa: E501
        :type number_of_shots: int
        """

        self._number_of_shots = number_of_shots

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
        if not isinstance(other, Job):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Job):
            return True

        return self.to_dict() != other.to_dict()