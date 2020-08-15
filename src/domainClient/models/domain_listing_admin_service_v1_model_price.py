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


class DomainListingAdminServiceV1ModelPrice(object):
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
        'display_text': 'str',
        '_from': 'int',
        'to': 'int'
    }

    attribute_map = {
        'display_text': 'displayText',
        '_from': 'from',
        'to': 'to'
    }

    def __init__(self, display_text=None, _from=None, to=None):  # noqa: E501
        """DomainListingAdminServiceV1ModelPrice - a model defined in Swagger"""  # noqa: E501

        self._display_text = None
        self.__from = None
        self._to = None
        self.discriminator = None

        if display_text is not None:
            self.display_text = display_text
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to

    @property
    def display_text(self):
        """Gets the display_text of this DomainListingAdminServiceV1ModelPrice.  # noqa: E501

        When provided this will be shown instead of the price range, e.g.: \\\"Offers over $450K considered\\\"  # noqa: E501

        :return: The display_text of this DomainListingAdminServiceV1ModelPrice.  # noqa: E501
        :rtype: str
        """
        return self._display_text

    @display_text.setter
    def display_text(self, display_text):
        """Sets the display_text of this DomainListingAdminServiceV1ModelPrice.

        When provided this will be shown instead of the price range, e.g.: \\\"Offers over $450K considered\\\"  # noqa: E501

        :param display_text: The display_text of this DomainListingAdminServiceV1ModelPrice.  # noqa: E501
        :type: str
        """

        self._display_text = display_text

    @property
    def _from(self):
        """Gets the _from of this DomainListingAdminServiceV1ModelPrice.  # noqa: E501

        Lowest price the property is expected to sell/rent for to set search price. For a fixed price, set this value the same as To  # noqa: E501

        :return: The _from of this DomainListingAdminServiceV1ModelPrice.  # noqa: E501
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this DomainListingAdminServiceV1ModelPrice.

        Lowest price the property is expected to sell/rent for to set search price. For a fixed price, set this value the same as To  # noqa: E501

        :param _from: The _from of this DomainListingAdminServiceV1ModelPrice.  # noqa: E501
        :type: int
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this DomainListingAdminServiceV1ModelPrice.  # noqa: E501

        Highest price the property is expected to sell/rent for to set search price. To should not be greater than 10% above From for sale listings (excl. new developments).               If the range provided is wider, it will be automatically corrected to be 10% around the same middle value.               For a fixed price, set this value the same as From  # noqa: E501

        :return: The to of this DomainListingAdminServiceV1ModelPrice.  # noqa: E501
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this DomainListingAdminServiceV1ModelPrice.

        Highest price the property is expected to sell/rent for to set search price. To should not be greater than 10% above From for sale listings (excl. new developments).               If the range provided is wider, it will be automatically corrected to be 10% around the same middle value.               For a fixed price, set this value the same as From  # noqa: E501

        :param to: The to of this DomainListingAdminServiceV1ModelPrice.  # noqa: E501
        :type: int
        """

        self._to = to

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
        if issubclass(DomainListingAdminServiceV1ModelPrice, dict):
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
        if not isinstance(other, DomainListingAdminServiceV1ModelPrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other