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


class DomainListingAdminServiceV1ModelSoldDetails(object):
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
        'sold_type': 'str',
        'sold_price': 'int',
        'display_sold_price': 'bool'
    }

    attribute_map = {
        'sold_type': 'soldType',
        'sold_price': 'soldPrice',
        'display_sold_price': 'displaySoldPrice'
    }

    def __init__(self, sold_type=None, sold_price=None, display_sold_price=None):  # noqa: E501
        """DomainListingAdminServiceV1ModelSoldDetails - a model defined in Swagger"""  # noqa: E501

        self._sold_type = None
        self._sold_price = None
        self._display_sold_price = None
        self.discriminator = None

        if sold_type is not None:
            self.sold_type = sold_type
        if sold_price is not None:
            self.sold_price = sold_price
        if display_sold_price is not None:
            self.display_sold_price = display_sold_price

    @property
    def sold_type(self):
        """Gets the sold_type of this DomainListingAdminServiceV1ModelSoldDetails.  # noqa: E501

        Sold Type  # noqa: E501

        :return: The sold_type of this DomainListingAdminServiceV1ModelSoldDetails.  # noqa: E501
        :rtype: str
        """
        return self._sold_type

    @sold_type.setter
    def sold_type(self, sold_type):
        """Sets the sold_type of this DomainListingAdminServiceV1ModelSoldDetails.

        Sold Type  # noqa: E501

        :param sold_type: The sold_type of this DomainListingAdminServiceV1ModelSoldDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["auction", "privateTreaty", "priorToAuction"]  # noqa: E501
        if sold_type not in allowed_values:
            raise ValueError(
                "Invalid value for `sold_type` ({0}), must be one of {1}"  # noqa: E501
                .format(sold_type, allowed_values)
            )

        self._sold_type = sold_type

    @property
    def sold_price(self):
        """Gets the sold_price of this DomainListingAdminServiceV1ModelSoldDetails.  # noqa: E501

        Price property was sold for  # noqa: E501

        :return: The sold_price of this DomainListingAdminServiceV1ModelSoldDetails.  # noqa: E501
        :rtype: int
        """
        return self._sold_price

    @sold_price.setter
    def sold_price(self, sold_price):
        """Sets the sold_price of this DomainListingAdminServiceV1ModelSoldDetails.

        Price property was sold for  # noqa: E501

        :param sold_price: The sold_price of this DomainListingAdminServiceV1ModelSoldDetails.  # noqa: E501
        :type: int
        """

        self._sold_price = sold_price

    @property
    def display_sold_price(self):
        """Gets the display_sold_price of this DomainListingAdminServiceV1ModelSoldDetails.  # noqa: E501

        Indicates how the price will be displayed for free to the general public, default to true if value not provided  # noqa: E501

        :return: The display_sold_price of this DomainListingAdminServiceV1ModelSoldDetails.  # noqa: E501
        :rtype: bool
        """
        return self._display_sold_price

    @display_sold_price.setter
    def display_sold_price(self, display_sold_price):
        """Sets the display_sold_price of this DomainListingAdminServiceV1ModelSoldDetails.

        Indicates how the price will be displayed for free to the general public, default to true if value not provided  # noqa: E501

        :param display_sold_price: The display_sold_price of this DomainListingAdminServiceV1ModelSoldDetails.  # noqa: E501
        :type: bool
        """

        self._display_sold_price = display_sold_price

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
        if issubclass(DomainListingAdminServiceV1ModelSoldDetails, dict):
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
        if not isinstance(other, DomainListingAdminServiceV1ModelSoldDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
