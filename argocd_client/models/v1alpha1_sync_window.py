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


class V1alpha1SyncWindow(object):
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
        'applications': 'list[str]',
        'clusters': 'list[str]',
        'duration': 'str',
        'kind': 'str',
        'manual_sync': 'bool',
        'namespaces': 'list[str]',
        'schedule': 'str'
    }

    attribute_map = {
        'applications': 'applications',
        'clusters': 'clusters',
        'duration': 'duration',
        'kind': 'kind',
        'manual_sync': 'manualSync',
        'namespaces': 'namespaces',
        'schedule': 'schedule'
    }

    def __init__(self, applications=None, clusters=None, duration=None, kind=None, manual_sync=None, namespaces=None, schedule=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1SyncWindow - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._applications = None
        self._clusters = None
        self._duration = None
        self._kind = None
        self._manual_sync = None
        self._namespaces = None
        self._schedule = None
        self.discriminator = None

        if applications is not None:
            self.applications = applications
        if clusters is not None:
            self.clusters = clusters
        if duration is not None:
            self.duration = duration
        if kind is not None:
            self.kind = kind
        if manual_sync is not None:
            self.manual_sync = manual_sync
        if namespaces is not None:
            self.namespaces = namespaces
        if schedule is not None:
            self.schedule = schedule

    @property
    def applications(self):
        """Gets the applications of this V1alpha1SyncWindow.  # noqa: E501


        :return: The applications of this V1alpha1SyncWindow.  # noqa: E501
        :rtype: list[str]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this V1alpha1SyncWindow.


        :param applications: The applications of this V1alpha1SyncWindow.  # noqa: E501
        :type: list[str]
        """

        self._applications = applications

    @property
    def clusters(self):
        """Gets the clusters of this V1alpha1SyncWindow.  # noqa: E501


        :return: The clusters of this V1alpha1SyncWindow.  # noqa: E501
        :rtype: list[str]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this V1alpha1SyncWindow.


        :param clusters: The clusters of this V1alpha1SyncWindow.  # noqa: E501
        :type: list[str]
        """

        self._clusters = clusters

    @property
    def duration(self):
        """Gets the duration of this V1alpha1SyncWindow.  # noqa: E501


        :return: The duration of this V1alpha1SyncWindow.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this V1alpha1SyncWindow.


        :param duration: The duration of this V1alpha1SyncWindow.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def kind(self):
        """Gets the kind of this V1alpha1SyncWindow.  # noqa: E501


        :return: The kind of this V1alpha1SyncWindow.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1alpha1SyncWindow.


        :param kind: The kind of this V1alpha1SyncWindow.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def manual_sync(self):
        """Gets the manual_sync of this V1alpha1SyncWindow.  # noqa: E501


        :return: The manual_sync of this V1alpha1SyncWindow.  # noqa: E501
        :rtype: bool
        """
        return self._manual_sync

    @manual_sync.setter
    def manual_sync(self, manual_sync):
        """Sets the manual_sync of this V1alpha1SyncWindow.


        :param manual_sync: The manual_sync of this V1alpha1SyncWindow.  # noqa: E501
        :type: bool
        """

        self._manual_sync = manual_sync

    @property
    def namespaces(self):
        """Gets the namespaces of this V1alpha1SyncWindow.  # noqa: E501


        :return: The namespaces of this V1alpha1SyncWindow.  # noqa: E501
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this V1alpha1SyncWindow.


        :param namespaces: The namespaces of this V1alpha1SyncWindow.  # noqa: E501
        :type: list[str]
        """

        self._namespaces = namespaces

    @property
    def schedule(self):
        """Gets the schedule of this V1alpha1SyncWindow.  # noqa: E501


        :return: The schedule of this V1alpha1SyncWindow.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this V1alpha1SyncWindow.


        :param schedule: The schedule of this V1alpha1SyncWindow.  # noqa: E501
        :type: str
        """

        self._schedule = schedule

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
        if not isinstance(other, V1alpha1SyncWindow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1SyncWindow):
            return True

        return self.to_dict() != other.to_dict()
