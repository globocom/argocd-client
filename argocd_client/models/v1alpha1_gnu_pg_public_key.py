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


class V1alpha1GnuPGPublicKey(object):
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
        'fingerprint': 'str',
        'key_data': 'str',
        'key_id': 'str',
        'owner': 'str',
        'sub_type': 'str',
        'trust': 'str'
    }

    attribute_map = {
        'fingerprint': 'fingerprint',
        'key_data': 'keyData',
        'key_id': 'keyID',
        'owner': 'owner',
        'sub_type': 'subType',
        'trust': 'trust'
    }

    def __init__(self, fingerprint=None, key_data=None, key_id=None, owner=None, sub_type=None, trust=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1GnuPGPublicKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fingerprint = None
        self._key_data = None
        self._key_id = None
        self._owner = None
        self._sub_type = None
        self._trust = None
        self.discriminator = None

        if fingerprint is not None:
            self.fingerprint = fingerprint
        if key_data is not None:
            self.key_data = key_data
        if key_id is not None:
            self.key_id = key_id
        if owner is not None:
            self.owner = owner
        if sub_type is not None:
            self.sub_type = sub_type
        if trust is not None:
            self.trust = trust

    @property
    def fingerprint(self):
        """Gets the fingerprint of this V1alpha1GnuPGPublicKey.  # noqa: E501


        :return: The fingerprint of this V1alpha1GnuPGPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this V1alpha1GnuPGPublicKey.


        :param fingerprint: The fingerprint of this V1alpha1GnuPGPublicKey.  # noqa: E501
        :type: str
        """

        self._fingerprint = fingerprint

    @property
    def key_data(self):
        """Gets the key_data of this V1alpha1GnuPGPublicKey.  # noqa: E501


        :return: The key_data of this V1alpha1GnuPGPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._key_data

    @key_data.setter
    def key_data(self, key_data):
        """Sets the key_data of this V1alpha1GnuPGPublicKey.


        :param key_data: The key_data of this V1alpha1GnuPGPublicKey.  # noqa: E501
        :type: str
        """

        self._key_data = key_data

    @property
    def key_id(self):
        """Gets the key_id of this V1alpha1GnuPGPublicKey.  # noqa: E501


        :return: The key_id of this V1alpha1GnuPGPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this V1alpha1GnuPGPublicKey.


        :param key_id: The key_id of this V1alpha1GnuPGPublicKey.  # noqa: E501
        :type: str
        """

        self._key_id = key_id

    @property
    def owner(self):
        """Gets the owner of this V1alpha1GnuPGPublicKey.  # noqa: E501


        :return: The owner of this V1alpha1GnuPGPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this V1alpha1GnuPGPublicKey.


        :param owner: The owner of this V1alpha1GnuPGPublicKey.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def sub_type(self):
        """Gets the sub_type of this V1alpha1GnuPGPublicKey.  # noqa: E501


        :return: The sub_type of this V1alpha1GnuPGPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this V1alpha1GnuPGPublicKey.


        :param sub_type: The sub_type of this V1alpha1GnuPGPublicKey.  # noqa: E501
        :type: str
        """

        self._sub_type = sub_type

    @property
    def trust(self):
        """Gets the trust of this V1alpha1GnuPGPublicKey.  # noqa: E501


        :return: The trust of this V1alpha1GnuPGPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._trust

    @trust.setter
    def trust(self, trust):
        """Sets the trust of this V1alpha1GnuPGPublicKey.


        :param trust: The trust of this V1alpha1GnuPGPublicKey.  # noqa: E501
        :type: str
        """

        self._trust = trust

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
        if not isinstance(other, V1alpha1GnuPGPublicKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1GnuPGPublicKey):
            return True

        return self.to_dict() != other.to_dict()
