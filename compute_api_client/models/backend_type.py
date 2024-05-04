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


class BackendType(object):
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
        'name': 'str',
        'infrastructure': 'str',
        'description': 'str',
        'image_id': 'str',
        'is_hardware': 'bool',
        'features': 'list[str]',
        'default_compiler_config': 'object',
        'native_gateset': 'object'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'infrastructure': 'infrastructure',
        'description': 'description',
        'image_id': 'image_id',
        'is_hardware': 'is_hardware',
        'features': 'features',
        'default_compiler_config': 'default_compiler_config',
        'native_gateset': 'native_gateset'
    }

    def __init__(self, id=None, name=None, infrastructure=None, description=None, image_id=None, is_hardware=None, features=None, default_compiler_config=None, native_gateset=None, local_vars_configuration=None):  # noqa: E501
        """BackendType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._infrastructure = None
        self._description = None
        self._image_id = None
        self._is_hardware = None
        self._features = None
        self._default_compiler_config = None
        self._native_gateset = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.infrastructure = infrastructure
        self.description = description
        self.image_id = image_id
        self.is_hardware = is_hardware
        self.features = features
        self.default_compiler_config = default_compiler_config
        self.native_gateset = native_gateset

    @property
    def id(self):
        """Gets the id of this BackendType.  # noqa: E501


        :return: The id of this BackendType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BackendType.


        :param id: The id of this BackendType.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this BackendType.  # noqa: E501


        :return: The name of this BackendType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BackendType.


        :param name: The name of this BackendType.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 32):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `32`")  # noqa: E501

        self._name = name

    @property
    def infrastructure(self):
        """Gets the infrastructure of this BackendType.  # noqa: E501


        :return: The infrastructure of this BackendType.  # noqa: E501
        :rtype: str
        """
        return self._infrastructure

    @infrastructure.setter
    def infrastructure(self, infrastructure):
        """Sets the infrastructure of this BackendType.


        :param infrastructure: The infrastructure of this BackendType.  # noqa: E501
        :type infrastructure: str
        """
        if self.local_vars_configuration.client_side_validation and infrastructure is None:  # noqa: E501
            raise ValueError("Invalid value for `infrastructure`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                infrastructure is not None and len(infrastructure) > 32):
            raise ValueError("Invalid value for `infrastructure`, length must be less than or equal to `32`")  # noqa: E501

        self._infrastructure = infrastructure

    @property
    def description(self):
        """Gets the description of this BackendType.  # noqa: E501


        :return: The description of this BackendType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BackendType.


        :param description: The description of this BackendType.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def image_id(self):
        """Gets the image_id of this BackendType.  # noqa: E501


        :return: The image_id of this BackendType.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this BackendType.


        :param image_id: The image_id of this BackendType.  # noqa: E501
        :type image_id: str
        """
        if self.local_vars_configuration.client_side_validation and image_id is None:  # noqa: E501
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                image_id is not None and len(image_id) > 16):
            raise ValueError("Invalid value for `image_id`, length must be less than or equal to `16`")  # noqa: E501

        self._image_id = image_id

    @property
    def is_hardware(self):
        """Gets the is_hardware of this BackendType.  # noqa: E501


        :return: The is_hardware of this BackendType.  # noqa: E501
        :rtype: bool
        """
        return self._is_hardware

    @is_hardware.setter
    def is_hardware(self, is_hardware):
        """Sets the is_hardware of this BackendType.


        :param is_hardware: The is_hardware of this BackendType.  # noqa: E501
        :type is_hardware: bool
        """
        if self.local_vars_configuration.client_side_validation and is_hardware is None:  # noqa: E501
            raise ValueError("Invalid value for `is_hardware`, must not be `None`")  # noqa: E501

        self._is_hardware = is_hardware

    @property
    def features(self):
        """Gets the features of this BackendType.  # noqa: E501


        :return: The features of this BackendType.  # noqa: E501
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this BackendType.


        :param features: The features of this BackendType.  # noqa: E501
        :type features: list[str]
        """
        if self.local_vars_configuration.client_side_validation and features is None:  # noqa: E501
            raise ValueError("Invalid value for `features`, must not be `None`")  # noqa: E501

        self._features = features

    @property
    def default_compiler_config(self):
        """Gets the default_compiler_config of this BackendType.  # noqa: E501


        :return: The default_compiler_config of this BackendType.  # noqa: E501
        :rtype: object
        """
        return self._default_compiler_config

    @default_compiler_config.setter
    def default_compiler_config(self, default_compiler_config):
        """Sets the default_compiler_config of this BackendType.


        :param default_compiler_config: The default_compiler_config of this BackendType.  # noqa: E501
        :type default_compiler_config: object
        """
        if self.local_vars_configuration.client_side_validation and default_compiler_config is None:  # noqa: E501
            raise ValueError("Invalid value for `default_compiler_config`, must not be `None`")  # noqa: E501

        self._default_compiler_config = default_compiler_config

    @property
    def native_gateset(self):
        """Gets the native_gateset of this BackendType.  # noqa: E501


        :return: The native_gateset of this BackendType.  # noqa: E501
        :rtype: object
        """
        return self._native_gateset

    @native_gateset.setter
    def native_gateset(self, native_gateset):
        """Sets the native_gateset of this BackendType.


        :param native_gateset: The native_gateset of this BackendType.  # noqa: E501
        :type native_gateset: object
        """
        if self.local_vars_configuration.client_side_validation and native_gateset is None:  # noqa: E501
            raise ValueError("Invalid value for `native_gateset`, must not be `None`")  # noqa: E501

        self._native_gateset = native_gateset

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
        if not isinstance(other, BackendType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackendType):
            return True

        return self.to_dict() != other.to_dict()