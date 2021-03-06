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


class V1alpha1SyncOperationResult(object):
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
        'resources': 'list[V1alpha1ResourceResult]',
        'revision': 'str',
        'source': 'V1alpha1ApplicationSource'
    }

    attribute_map = {
        'resources': 'resources',
        'revision': 'revision',
        'source': 'source'
    }

    def __init__(self, resources=None, revision=None, source=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1SyncOperationResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._resources = None
        self._revision = None
        self._source = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if revision is not None:
            self.revision = revision
        if source is not None:
            self.source = source

    @property
    def resources(self):
        """Gets the resources of this V1alpha1SyncOperationResult.  # noqa: E501


        :return: The resources of this V1alpha1SyncOperationResult.  # noqa: E501
        :rtype: list[V1alpha1ResourceResult]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this V1alpha1SyncOperationResult.


        :param resources: The resources of this V1alpha1SyncOperationResult.  # noqa: E501
        :type: list[V1alpha1ResourceResult]
        """

        self._resources = resources

    @property
    def revision(self):
        """Gets the revision of this V1alpha1SyncOperationResult.  # noqa: E501


        :return: The revision of this V1alpha1SyncOperationResult.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this V1alpha1SyncOperationResult.


        :param revision: The revision of this V1alpha1SyncOperationResult.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def source(self):
        """Gets the source of this V1alpha1SyncOperationResult.  # noqa: E501


        :return: The source of this V1alpha1SyncOperationResult.  # noqa: E501
        :rtype: V1alpha1ApplicationSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this V1alpha1SyncOperationResult.


        :param source: The source of this V1alpha1SyncOperationResult.  # noqa: E501
        :type: V1alpha1ApplicationSource
        """

        self._source = source

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
        if not isinstance(other, V1alpha1SyncOperationResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1SyncOperationResult):
            return True

        return self.to_dict() != other.to_dict()
