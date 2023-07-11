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


class File(object):
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
        'content': 'str',
        'compile_stage': 'CompileStage',
        'compile_properties': 'object',
        'generated': 'bool',
        'commit_id': 'int',
        'language_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'content': 'content',
        'compile_stage': 'compile_stage',
        'compile_properties': 'compile_properties',
        'generated': 'generated',
        'commit_id': 'commit_id',
        'language_id': 'language_id'
    }

    def __init__(self, id=None, content=None, compile_stage=None, compile_properties=None, generated=False, commit_id=None, language_id=None, local_vars_configuration=None):  # noqa: E501
        """File - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._content = None
        self._compile_stage = None
        self._compile_properties = None
        self._generated = None
        self._commit_id = None
        self._language_id = None
        self.discriminator = None

        self.id = id
        self.content = content
        self.compile_stage = compile_stage
        self.compile_properties = compile_properties
        if generated is not None:
            self.generated = generated
        self.commit_id = commit_id
        self.language_id = language_id

    @property
    def id(self):
        """Gets the id of this File.  # noqa: E501


        :return: The id of this File.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this File.


        :param id: The id of this File.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and id < 1):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def content(self):
        """Gets the content of this File.  # noqa: E501


        :return: The content of this File.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this File.


        :param content: The content of this File.  # noqa: E501
        :type content: str
        """
        if self.local_vars_configuration.client_side_validation and content is None:  # noqa: E501
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def compile_stage(self):
        """Gets the compile_stage of this File.  # noqa: E501

        NONE: none<br/>MAPPED: mapped<br/>NATIVE_GATESET: native_gateset<br/>SCHEDULED: scheduled  # noqa: E501

        :return: The compile_stage of this File.  # noqa: E501
        :rtype: CompileStage
        """
        return self._compile_stage

    @compile_stage.setter
    def compile_stage(self, compile_stage):
        """Sets the compile_stage of this File.

        NONE: none<br/>MAPPED: mapped<br/>NATIVE_GATESET: native_gateset<br/>SCHEDULED: scheduled  # noqa: E501

        :param compile_stage: The compile_stage of this File.  # noqa: E501
        :type compile_stage: CompileStage
        """
        if self.local_vars_configuration.client_side_validation and compile_stage is None:  # noqa: E501
            raise ValueError("Invalid value for `compile_stage`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                compile_stage is not None and len(compile_stage) > 14):
            raise ValueError("Invalid value for `compile_stage`, length must be less than or equal to `14`")  # noqa: E501

        self._compile_stage = compile_stage

    @property
    def compile_properties(self):
        """Gets the compile_properties of this File.  # noqa: E501


        :return: The compile_properties of this File.  # noqa: E501
        :rtype: object
        """
        return self._compile_properties

    @compile_properties.setter
    def compile_properties(self, compile_properties):
        """Sets the compile_properties of this File.


        :param compile_properties: The compile_properties of this File.  # noqa: E501
        :type compile_properties: object
        """

        self._compile_properties = compile_properties

    @property
    def generated(self):
        """Gets the generated of this File.  # noqa: E501


        :return: The generated of this File.  # noqa: E501
        :rtype: bool
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this File.


        :param generated: The generated of this File.  # noqa: E501
        :type generated: bool
        """

        self._generated = generated

    @property
    def commit_id(self):
        """Gets the commit_id of this File.  # noqa: E501


        :return: The commit_id of this File.  # noqa: E501
        :rtype: int
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this File.


        :param commit_id: The commit_id of this File.  # noqa: E501
        :type commit_id: int
        """
        if self.local_vars_configuration.client_side_validation and commit_id is None:  # noqa: E501
            raise ValueError("Invalid value for `commit_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                commit_id is not None and commit_id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `commit_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                commit_id is not None and commit_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `commit_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._commit_id = commit_id

    @property
    def language_id(self):
        """Gets the language_id of this File.  # noqa: E501


        :return: The language_id of this File.  # noqa: E501
        :rtype: int
        """
        return self._language_id

    @language_id.setter
    def language_id(self, language_id):
        """Sets the language_id of this File.


        :param language_id: The language_id of this File.  # noqa: E501
        :type language_id: int
        """
        if self.local_vars_configuration.client_side_validation and language_id is None:  # noqa: E501
            raise ValueError("Invalid value for `language_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                language_id is not None and language_id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `language_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                language_id is not None and language_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `language_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._language_id = language_id

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
        if not isinstance(other, File):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, File):
            return True

        return self.to_dict() != other.to_dict()
