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


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails(object):
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
        'hidden_reasons': 'list[str]',
        'gst_option': 'str',
        'price_type': 'str',
        'price_unit': 'str',
        'price': 'float',
        'price_from': 'int',
        'price_to': 'int',
        'price_prefix': 'str',
        'can_display_price': 'bool',
        'display_price': 'str',
        'bond': 'float',
        'price_reduction': 'bool'
    }

    attribute_map = {
        'hidden_reasons': 'hiddenReasons',
        'gst_option': 'gstOption',
        'price_type': 'priceType',
        'price_unit': 'priceUnit',
        'price': 'price',
        'price_from': 'priceFrom',
        'price_to': 'priceTo',
        'price_prefix': 'pricePrefix',
        'can_display_price': 'canDisplayPrice',
        'display_price': 'displayPrice',
        'bond': 'bond',
        'price_reduction': 'priceReduction'
    }

    def __init__(self, hidden_reasons=None, gst_option=None, price_type=None, price_unit=None, price=None, price_from=None, price_to=None, price_prefix=None, can_display_price=None, display_price=None, bond=None, price_reduction=None):  # noqa: E501
        """DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails - a model defined in Swagger"""  # noqa: E501

        self._hidden_reasons = None
        self._gst_option = None
        self._price_type = None
        self._price_unit = None
        self._price = None
        self._price_from = None
        self._price_to = None
        self._price_prefix = None
        self._can_display_price = None
        self._display_price = None
        self._bond = None
        self._price_reduction = None
        self.discriminator = None

        if hidden_reasons is not None:
            self.hidden_reasons = hidden_reasons
        if gst_option is not None:
            self.gst_option = gst_option
        if price_type is not None:
            self.price_type = price_type
        if price_unit is not None:
            self.price_unit = price_unit
        if price is not None:
            self.price = price
        if price_from is not None:
            self.price_from = price_from
        if price_to is not None:
            self.price_to = price_to
        if price_prefix is not None:
            self.price_prefix = price_prefix
        if can_display_price is not None:
            self.can_display_price = can_display_price
        if display_price is not None:
            self.display_price = display_price
        if bond is not None:
            self.bond = bond
        if price_reduction is not None:
            self.price_reduction = price_reduction

    @property
    def hidden_reasons(self):
        """Gets the hidden_reasons of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501


        :return: The hidden_reasons of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._hidden_reasons

    @hidden_reasons.setter
    def hidden_reasons(self, hidden_reasons):
        """Sets the hidden_reasons of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.


        :param hidden_reasons: The hidden_reasons of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["byAgency", "qLDRestriction"]  # noqa: E501
        if not set(hidden_reasons).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `hidden_reasons` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(hidden_reasons) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._hidden_reasons = hidden_reasons

    @property
    def gst_option(self):
        """Gets the gst_option of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501


        :return: The gst_option of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :rtype: str
        """
        return self._gst_option

    @gst_option.setter
    def gst_option(self, gst_option):
        """Sets the gst_option of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.


        :param gst_option: The gst_option of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["na", "inc", "ex"]  # noqa: E501
        if gst_option not in allowed_values:
            raise ValueError(
                "Invalid value for `gst_option` ({0}), must be one of {1}"  # noqa: E501
                .format(gst_option, allowed_values)
            )

        self._gst_option = gst_option

    @property
    def price_type(self):
        """Gets the price_type of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501


        :return: The price_type of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :rtype: str
        """
        return self._price_type

    @price_type.setter
    def price_type(self, price_type):
        """Sets the price_type of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.


        :param price_type: The price_type of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["gross", "net"]  # noqa: E501
        if price_type not in allowed_values:
            raise ValueError(
                "Invalid value for `price_type` ({0}), must be one of {1}"  # noqa: E501
                .format(price_type, allowed_values)
            )

        self._price_type = price_type

    @property
    def price_unit(self):
        """Gets the price_unit of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501


        :return: The price_unit of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :rtype: str
        """
        return self._price_unit

    @price_unit.setter
    def price_unit(self, price_unit):
        """Sets the price_unit of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.


        :param price_unit: The price_unit of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["totalAmount", "perSqm"]  # noqa: E501
        if price_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `price_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(price_unit, allowed_values)
            )

        self._price_unit = price_unit

    @property
    def price(self):
        """Gets the price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501


        :return: The price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.


        :param price: The price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def price_from(self):
        """Gets the price_from of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501


        :return: The price_from of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :rtype: int
        """
        return self._price_from

    @price_from.setter
    def price_from(self, price_from):
        """Sets the price_from of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.


        :param price_from: The price_from of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :type: int
        """

        self._price_from = price_from

    @property
    def price_to(self):
        """Gets the price_to of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501


        :return: The price_to of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :rtype: int
        """
        return self._price_to

    @price_to.setter
    def price_to(self, price_to):
        """Sets the price_to of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.


        :param price_to: The price_to of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :type: int
        """

        self._price_to = price_to

    @property
    def price_prefix(self):
        """Gets the price_prefix of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501


        :return: The price_prefix of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :rtype: str
        """
        return self._price_prefix

    @price_prefix.setter
    def price_prefix(self, price_prefix):
        """Sets the price_prefix of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.


        :param price_prefix: The price_prefix of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :type: str
        """

        self._price_prefix = price_prefix

    @property
    def can_display_price(self):
        """Gets the can_display_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501


        :return: The can_display_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :rtype: bool
        """
        return self._can_display_price

    @can_display_price.setter
    def can_display_price(self, can_display_price):
        """Sets the can_display_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.


        :param can_display_price: The can_display_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :type: bool
        """

        self._can_display_price = can_display_price

    @property
    def display_price(self):
        """Gets the display_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501


        :return: The display_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :rtype: str
        """
        return self._display_price

    @display_price.setter
    def display_price(self, display_price):
        """Sets the display_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.


        :param display_price: The display_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :type: str
        """

        self._display_price = display_price

    @property
    def bond(self):
        """Gets the bond of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501


        :return: The bond of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :rtype: float
        """
        return self._bond

    @bond.setter
    def bond(self, bond):
        """Sets the bond of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.


        :param bond: The bond of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :type: float
        """

        self._bond = bond

    @property
    def price_reduction(self):
        """Gets the price_reduction of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501


        :return: The price_reduction of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :rtype: bool
        """
        return self._price_reduction

    @price_reduction.setter
    def price_reduction(self, price_reduction):
        """Sets the price_reduction of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.


        :param price_reduction: The price_reduction of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails.  # noqa: E501
        :type: bool
        """

        self._price_reduction = price_reduction

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
        if issubclass(DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails, dict):
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
        if not isinstance(other, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
