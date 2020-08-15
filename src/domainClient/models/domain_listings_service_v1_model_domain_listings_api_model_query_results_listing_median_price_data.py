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


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData(object):
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
        'price_type': 'str',
        'suburb': 'str',
        'postcode': 'str',
        'median_price': 'int',
        'source': 'str',
        'source_date_from': 'str',
        'source_date_to': 'str',
        'source_collection_date': 'str'
    }

    attribute_map = {
        'price_type': 'priceType',
        'suburb': 'suburb',
        'postcode': 'postcode',
        'median_price': 'medianPrice',
        'source': 'source',
        'source_date_from': 'sourceDateFrom',
        'source_date_to': 'sourceDateTo',
        'source_collection_date': 'sourceCollectionDate'
    }

    def __init__(self, price_type=None, suburb=None, postcode=None, median_price=None, source=None, source_date_from=None, source_date_to=None, source_collection_date=None):  # noqa: E501
        """DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData - a model defined in Swagger"""  # noqa: E501

        self._price_type = None
        self._suburb = None
        self._postcode = None
        self._median_price = None
        self._source = None
        self._source_date_from = None
        self._source_date_to = None
        self._source_collection_date = None
        self.discriminator = None

        if price_type is not None:
            self.price_type = price_type
        if suburb is not None:
            self.suburb = suburb
        if postcode is not None:
            self.postcode = postcode
        if median_price is not None:
            self.median_price = median_price
        if source is not None:
            self.source = source
        if source_date_from is not None:
            self.source_date_from = source_date_from
        if source_date_to is not None:
            self.source_date_to = source_date_to
        if source_collection_date is not None:
            self.source_collection_date = source_collection_date

    @property
    def price_type(self):
        """Gets the price_type of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501


        :return: The price_type of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501
        :rtype: str
        """
        return self._price_type

    @price_type.setter
    def price_type(self, price_type):
        """Sets the price_type of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.


        :param price_type: The price_type of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501
        :type: str
        """
        allowed_values = ["house", "apartmentUnitFlat", "vacantLand"]  # noqa: E501
        if price_type not in allowed_values:
            raise ValueError(
                "Invalid value for `price_type` ({0}), must be one of {1}"  # noqa: E501
                .format(price_type, allowed_values)
            )

        self._price_type = price_type

    @property
    def suburb(self):
        """Gets the suburb of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501


        :return: The suburb of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501
        :rtype: str
        """
        return self._suburb

    @suburb.setter
    def suburb(self, suburb):
        """Sets the suburb of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.


        :param suburb: The suburb of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501
        :type: str
        """

        self._suburb = suburb

    @property
    def postcode(self):
        """Gets the postcode of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501


        :return: The postcode of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.


        :param postcode: The postcode of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

    @property
    def median_price(self):
        """Gets the median_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501


        :return: The median_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501
        :rtype: int
        """
        return self._median_price

    @median_price.setter
    def median_price(self, median_price):
        """Sets the median_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.


        :param median_price: The median_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501
        :type: int
        """

        self._median_price = median_price

    @property
    def source(self):
        """Gets the source of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501


        :return: The source of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.


        :param source: The source of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def source_date_from(self):
        """Gets the source_date_from of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501


        :return: The source_date_from of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501
        :rtype: str
        """
        return self._source_date_from

    @source_date_from.setter
    def source_date_from(self, source_date_from):
        """Sets the source_date_from of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.


        :param source_date_from: The source_date_from of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501
        :type: str
        """

        self._source_date_from = source_date_from

    @property
    def source_date_to(self):
        """Gets the source_date_to of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501


        :return: The source_date_to of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501
        :rtype: str
        """
        return self._source_date_to

    @source_date_to.setter
    def source_date_to(self, source_date_to):
        """Sets the source_date_to of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.


        :param source_date_to: The source_date_to of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501
        :type: str
        """

        self._source_date_to = source_date_to

    @property
    def source_collection_date(self):
        """Gets the source_collection_date of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501


        :return: The source_collection_date of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501
        :rtype: str
        """
        return self._source_collection_date

    @source_collection_date.setter
    def source_collection_date(self, source_collection_date):
        """Sets the source_collection_date of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.


        :param source_collection_date: The source_collection_date of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData.  # noqa: E501
        :type: str
        """

        self._source_collection_date = source_collection_date

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
        if issubclass(DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData, dict):
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
        if not isinstance(other, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other