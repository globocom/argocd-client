# coding: utf-8

"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argocd_client.configuration import Configuration


class V1alpha1Command(object):
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
        'args': 'list[str]',
        'command': 'list[str]'
    }

    attribute_map = {
        'args': 'args',
        'command': 'command'
    }

    def __init__(self, args=None, command=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1Command - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._args = None
        self._command = None
        self.discriminator = None

        if args is not None:
            self.args = args
        if command is not None:
            self.command = command

    @property
    def args(self):
        """Gets the args of this V1alpha1Command.  # noqa: E501


        :return: The args of this V1alpha1Command.  # noqa: E501
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this V1alpha1Command.


        :param args: The args of this V1alpha1Command.  # noqa: E501
        :type: list[str]
        """

        self._args = args

    @property
    def command(self):
        """Gets the command of this V1alpha1Command.  # noqa: E501


        :return: The command of this V1alpha1Command.  # noqa: E501
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this V1alpha1Command.


        :param command: The command of this V1alpha1Command.  # noqa: E501
        :type: list[str]
        """

        self._command = command

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1Command):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1Command):
            return True

        return self.to_dict() != other.to_dict()