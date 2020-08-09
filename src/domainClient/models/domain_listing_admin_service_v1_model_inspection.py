# coding: utf-8

"""
    Domain Group API V1

    Provides public access to Domain's microservices  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DomainListingAdminServiceV1ModelInspection(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        '_from': 'datetime',
        'to': 'datetime',
        'repeat': 'bool'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'repeat': 'repeat'
    }

    def __init__(self, _from=None, to=None, repeat=None):  # noqa: E501
        """DomainListingAdminServiceV1ModelInspection - a model defined in Swagger"""  # noqa: E501

        self.__from = None
        self._to = None
        self._repeat = None
        self.discriminator = None

        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if repeat is not None:
            self.repeat = repeat

    @property
    def _from(self):
        """Gets the _from of this DomainListingAdminServiceV1ModelInspection.  # noqa: E501

        Format: yyyy-mm-dd HH:mm:ss eg: 2015-10-20 13:30:00  # noqa: E501

        :return: The _from of this DomainListingAdminServiceV1ModelInspection.  # noqa: E501
        :rtype: datetime
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this DomainListingAdminServiceV1ModelInspection.

        Format: yyyy-mm-dd HH:mm:ss eg: 2015-10-20 13:30:00  # noqa: E501

        :param _from: The _from of this DomainListingAdminServiceV1ModelInspection.  # noqa: E501
        :type: datetime
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this DomainListingAdminServiceV1ModelInspection.  # noqa: E501

        Format: yyyy-mm-dd HH:mm:ss, eg: 2015-10-20 14:30:00  # noqa: E501

        :return: The to of this DomainListingAdminServiceV1ModelInspection.  # noqa: E501
        :rtype: datetime
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this DomainListingAdminServiceV1ModelInspection.

        Format: yyyy-mm-dd HH:mm:ss, eg: 2015-10-20 14:30:00  # noqa: E501

        :param to: The to of this DomainListingAdminServiceV1ModelInspection.  # noqa: E501
        :type: datetime
        """

        self._to = to

    @property
    def repeat(self):
        """Gets the repeat of this DomainListingAdminServiceV1ModelInspection.  # noqa: E501

        Specifies if the inspection is recurring weekly  # noqa: E501

        :return: The repeat of this DomainListingAdminServiceV1ModelInspection.  # noqa: E501
        :rtype: bool
        """
        return self._repeat

    @repeat.setter
    def repeat(self, repeat):
        """Sets the repeat of this DomainListingAdminServiceV1ModelInspection.

        Specifies if the inspection is recurring weekly  # noqa: E501

        :param repeat: The repeat of this DomainListingAdminServiceV1ModelInspection.  # noqa: E501
        :type: bool
        """

        self._repeat = repeat

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DomainListingAdminServiceV1ModelInspection, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DomainListingAdminServiceV1ModelInspection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
