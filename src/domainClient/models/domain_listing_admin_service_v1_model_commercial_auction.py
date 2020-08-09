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


class DomainListingAdminServiceV1ModelCommercialAuction(object):
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
        'auction_terms': 'str',
        'date_time': 'datetime',
        'location': 'str'
    }

    attribute_map = {
        'auction_terms': 'auctionTerms',
        'date_time': 'dateTime',
        'location': 'location'
    }

    def __init__(self, auction_terms=None, date_time=None, location=None):  # noqa: E501
        """DomainListingAdminServiceV1ModelCommercialAuction - a model defined in Swagger"""  # noqa: E501

        self._auction_terms = None
        self._date_time = None
        self._location = None
        self.discriminator = None

        if auction_terms is not None:
            self.auction_terms = auction_terms
        if date_time is not None:
            self.date_time = date_time
        if location is not None:
            self.location = location

    @property
    def auction_terms(self):
        """Gets the auction_terms of this DomainListingAdminServiceV1ModelCommercialAuction.  # noqa: E501

        Terms for the auctions, up to 200 characters. Example: \\\"10% deposit, balance 60 days\\\"  # noqa: E501

        :return: The auction_terms of this DomainListingAdminServiceV1ModelCommercialAuction.  # noqa: E501
        :rtype: str
        """
        return self._auction_terms

    @auction_terms.setter
    def auction_terms(self, auction_terms):
        """Sets the auction_terms of this DomainListingAdminServiceV1ModelCommercialAuction.

        Terms for the auctions, up to 200 characters. Example: \\\"10% deposit, balance 60 days\\\"  # noqa: E501

        :param auction_terms: The auction_terms of this DomainListingAdminServiceV1ModelCommercialAuction.  # noqa: E501
        :type: str
        """

        self._auction_terms = auction_terms

    @property
    def date_time(self):
        """Gets the date_time of this DomainListingAdminServiceV1ModelCommercialAuction.  # noqa: E501

        Date of the auction. format: yyyy-MM-ddTHH:mm:ss  # noqa: E501

        :return: The date_time of this DomainListingAdminServiceV1ModelCommercialAuction.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this DomainListingAdminServiceV1ModelCommercialAuction.

        Date of the auction. format: yyyy-MM-ddTHH:mm:ss  # noqa: E501

        :param date_time: The date_time of this DomainListingAdminServiceV1ModelCommercialAuction.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

    @property
    def location(self):
        """Gets the location of this DomainListingAdminServiceV1ModelCommercialAuction.  # noqa: E501

        Optional. Venue for the Auction. String max 100 characters. If the Location is omitted, or included but empty, the Venue will default to \\\"On Site\\\".  # noqa: E501

        :return: The location of this DomainListingAdminServiceV1ModelCommercialAuction.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this DomainListingAdminServiceV1ModelCommercialAuction.

        Optional. Venue for the Auction. String max 100 characters. If the Location is omitted, or included but empty, the Venue will default to \\\"On Site\\\".  # noqa: E501

        :param location: The location of this DomainListingAdminServiceV1ModelCommercialAuction.  # noqa: E501
        :type: str
        """

        self._location = location

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
        if issubclass(DomainListingAdminServiceV1ModelCommercialAuction, dict):
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
        if not isinstance(other, DomainListingAdminServiceV1ModelCommercialAuction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
