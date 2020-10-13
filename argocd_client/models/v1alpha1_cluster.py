# coding: utf-8
# Copyright (c) 2020, Globo (https://github.com/globocom)
# License: BSD-3-Clause

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


class V1alpha1Cluster(object):
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
        'config': 'V1alpha1ClusterConfig',
        'connection_state': 'V1alpha1ConnectionState',
        'info': 'V1alpha1ClusterInfo',
        'name': 'str',
        'namespaces': 'list[str]',
        'refresh_requested_at': 'V1Time',
        'server': 'str',
        'server_version': 'str'
    }

    attribute_map = {
        'config': 'config',
        'connection_state': 'connectionState',
        'info': 'info',
        'name': 'name',
        'namespaces': 'namespaces',
        'refresh_requested_at': 'refreshRequestedAt',
        'server': 'server',
        'server_version': 'serverVersion'
    }

    def __init__(self, config=None, connection_state=None, info=None, name=None, namespaces=None, refresh_requested_at=None, server=None, server_version=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1Cluster - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._config = None
        self._connection_state = None
        self._info = None
        self._name = None
        self._namespaces = None
        self._refresh_requested_at = None
        self._server = None
        self._server_version = None
        self.discriminator = None

        if config is not None:
            self.config = config
        if connection_state is not None:
            self.connection_state = connection_state
        if info is not None:
            self.info = info
        if name is not None:
            self.name = name
        if namespaces is not None:
            self.namespaces = namespaces
        if refresh_requested_at is not None:
            self.refresh_requested_at = refresh_requested_at
        if server is not None:
            self.server = server
        if server_version is not None:
            self.server_version = server_version

    @property
    def config(self):
        """Gets the config of this V1alpha1Cluster.  # noqa: E501


        :return: The config of this V1alpha1Cluster.  # noqa: E501
        :rtype: V1alpha1ClusterConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this V1alpha1Cluster.


        :param config: The config of this V1alpha1Cluster.  # noqa: E501
        :type: V1alpha1ClusterConfig
        """

        self._config = config

    @property
    def connection_state(self):
        """Gets the connection_state of this V1alpha1Cluster.  # noqa: E501


        :return: The connection_state of this V1alpha1Cluster.  # noqa: E501
        :rtype: V1alpha1ConnectionState
        """
        return self._connection_state

    @connection_state.setter
    def connection_state(self, connection_state):
        """Sets the connection_state of this V1alpha1Cluster.


        :param connection_state: The connection_state of this V1alpha1Cluster.  # noqa: E501
        :type: V1alpha1ConnectionState
        """

        self._connection_state = connection_state

    @property
    def info(self):
        """Gets the info of this V1alpha1Cluster.  # noqa: E501


        :return: The info of this V1alpha1Cluster.  # noqa: E501
        :rtype: V1alpha1ClusterInfo
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this V1alpha1Cluster.


        :param info: The info of this V1alpha1Cluster.  # noqa: E501
        :type: V1alpha1ClusterInfo
        """

        self._info = info

    @property
    def name(self):
        """Gets the name of this V1alpha1Cluster.  # noqa: E501


        :return: The name of this V1alpha1Cluster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1Cluster.


        :param name: The name of this V1alpha1Cluster.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespaces(self):
        """Gets the namespaces of this V1alpha1Cluster.  # noqa: E501

        Holds list of namespaces which are accessible in that cluster. Cluster level resources would be ignored if namespace list is not empty.  # noqa: E501

        :return: The namespaces of this V1alpha1Cluster.  # noqa: E501
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this V1alpha1Cluster.

        Holds list of namespaces which are accessible in that cluster. Cluster level resources would be ignored if namespace list is not empty.  # noqa: E501

        :param namespaces: The namespaces of this V1alpha1Cluster.  # noqa: E501
        :type: list[str]
        """

        self._namespaces = namespaces

    @property
    def refresh_requested_at(self):
        """Gets the refresh_requested_at of this V1alpha1Cluster.  # noqa: E501


        :return: The refresh_requested_at of this V1alpha1Cluster.  # noqa: E501
        :rtype: V1Time
        """
        return self._refresh_requested_at

    @refresh_requested_at.setter
    def refresh_requested_at(self, refresh_requested_at):
        """Sets the refresh_requested_at of this V1alpha1Cluster.


        :param refresh_requested_at: The refresh_requested_at of this V1alpha1Cluster.  # noqa: E501
        :type: V1Time
        """

        self._refresh_requested_at = refresh_requested_at

    @property
    def server(self):
        """Gets the server of this V1alpha1Cluster.  # noqa: E501


        :return: The server of this V1alpha1Cluster.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this V1alpha1Cluster.


        :param server: The server of this V1alpha1Cluster.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def server_version(self):
        """Gets the server_version of this V1alpha1Cluster.  # noqa: E501


        :return: The server_version of this V1alpha1Cluster.  # noqa: E501
        :rtype: str
        """
        return self._server_version

    @server_version.setter
    def server_version(self, server_version):
        """Sets the server_version of this V1alpha1Cluster.


        :param server_version: The server_version of this V1alpha1Cluster.  # noqa: E501
        :type: str
        """

        self._server_version = server_version

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
        if not isinstance(other, V1alpha1Cluster):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1Cluster):
            return True

        return self.to_dict() != other.to_dict()
