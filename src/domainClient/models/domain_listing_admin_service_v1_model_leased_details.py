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


class DomainListingAdminServiceV1ModelLeasedDetails(object):
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
        'leased_price': 'int',
        'leased_duration': 'int'
    }

    attribute_map = {
        'leased_price': 'leasedPrice',
        'leased_duration': 'leasedDuration'
    }

    def __init__(self, leased_price=None, leased_duration=None):  # noqa: E501
        """DomainListingAdminServiceV1ModelLeasedDetails - a model defined in Swagger"""  # noqa: E501

        self._leased_price = None
        self._leased_duration = None
        self.discriminator = None

        if leased_price is not None:
            self.leased_price = leased_price
        if leased_duration is not None:
            self.leased_duration = leased_duration

    @property
    def leased_price(self):
        """Gets the leased_price of this DomainListingAdminServiceV1ModelLeasedDetails.  # noqa: E501

        Optional. The weekly rental price.  # noqa: E501

        :return: The leased_price of this DomainListingAdminServiceV1ModelLeasedDetails.  # noqa: E501
        :rtype: int
        """
        return self._leased_price

    @leased_price.setter
    def leased_price(self, leased_price):
        """Sets the leased_price of this DomainListingAdminServiceV1ModelLeasedDetails.

        Optional. The weekly rental price.  # noqa: E501

        :param leased_price: The leased_price of this DomainListingAdminServiceV1ModelLeasedDetails.  # noqa: E501
        :type: int
        """

        self._leased_price = leased_price

    @property
    def leased_duration(self):
        """Gets the leased_duration of this DomainListingAdminServiceV1ModelLeasedDetails.  # noqa: E501

        The duration of the lease in weeks.  # noqa: E501

        :return: The leased_duration of this DomainListingAdminServiceV1ModelLeasedDetails.  # noqa: E501
        :rtype: int
        """
        return self._leased_duration

    @leased_duration.setter
    def leased_duration(self, leased_duration):
        """Sets the leased_duration of this DomainListingAdminServiceV1ModelLeasedDetails.

        The duration of the lease in weeks.  # noqa: E501

        :param leased_duration: The leased_duration of this DomainListingAdminServiceV1ModelLeasedDetails.  # noqa: E501
        :type: int
        """

        self._leased_duration = leased_duration

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
        if issubclass(DomainListingAdminServiceV1ModelLeasedDetails, dict):
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
        if not isinstance(other, DomainListingAdminServiceV1ModelLeasedDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
