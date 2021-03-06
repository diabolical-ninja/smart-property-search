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


class DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate(object):
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
        'price_confidence': 'str',
        '_date': 'datetime',
        'lower_price': 'int',
        'upper_price': 'int',
        'mid_price': 'int',
        'history': 'list[DomainPublicAdapterWebApiModelsV1PropertiesHistoricalPriceEstimate]'
    }

    attribute_map = {
        'price_confidence': 'priceConfidence',
        '_date': 'date',
        'lower_price': 'lowerPrice',
        'upper_price': 'upperPrice',
        'mid_price': 'midPrice',
        'history': 'history'
    }

    def __init__(self, price_confidence=None, _date=None, lower_price=None, upper_price=None, mid_price=None, history=None):  # noqa: E501
        """DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate - a model defined in Swagger"""  # noqa: E501

        self._price_confidence = None
        self.__date = None
        self._lower_price = None
        self._upper_price = None
        self._mid_price = None
        self._history = None
        self.discriminator = None

        if price_confidence is not None:
            self.price_confidence = price_confidence
        if _date is not None:
            self._date = _date
        if lower_price is not None:
            self.lower_price = lower_price
        if upper_price is not None:
            self.upper_price = upper_price
        if mid_price is not None:
            self.mid_price = mid_price
        if history is not None:
            self.history = history

    @property
    def price_confidence(self):
        """Gets the price_confidence of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501

        Gets or sets the confidence.  # noqa: E501

        :return: The price_confidence of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501
        :rtype: str
        """
        return self._price_confidence

    @price_confidence.setter
    def price_confidence(self, price_confidence):
        """Sets the price_confidence of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.

        Gets or sets the confidence.  # noqa: E501

        :param price_confidence: The price_confidence of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501
        :type: str
        """
        allowed_values = ["high", "medium", "recentlySold"]  # noqa: E501
        if price_confidence not in allowed_values:
            raise ValueError(
                "Invalid value for `price_confidence` ({0}), must be one of {1}"  # noqa: E501
                .format(price_confidence, allowed_values)
            )

        self._price_confidence = price_confidence

    @property
    def _date(self):
        """Gets the _date of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501

        Gets or sets the date.  # noqa: E501

        :return: The _date of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.

        Gets or sets the date.  # noqa: E501

        :param _date: The _date of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def lower_price(self):
        """Gets the lower_price of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501

        Gets or sets the lower price.  # noqa: E501

        :return: The lower_price of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501
        :rtype: int
        """
        return self._lower_price

    @lower_price.setter
    def lower_price(self, lower_price):
        """Sets the lower_price of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.

        Gets or sets the lower price.  # noqa: E501

        :param lower_price: The lower_price of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501
        :type: int
        """

        self._lower_price = lower_price

    @property
    def upper_price(self):
        """Gets the upper_price of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501

        Gets or sets the upper price.  # noqa: E501

        :return: The upper_price of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501
        :rtype: int
        """
        return self._upper_price

    @upper_price.setter
    def upper_price(self, upper_price):
        """Sets the upper_price of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.

        Gets or sets the upper price.  # noqa: E501

        :param upper_price: The upper_price of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501
        :type: int
        """

        self._upper_price = upper_price

    @property
    def mid_price(self):
        """Gets the mid_price of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501

        Mid Price. Average of Upper and Lower  # noqa: E501

        :return: The mid_price of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501
        :rtype: int
        """
        return self._mid_price

    @mid_price.setter
    def mid_price(self, mid_price):
        """Sets the mid_price of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.

        Mid Price. Average of Upper and Lower  # noqa: E501

        :param mid_price: The mid_price of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501
        :type: int
        """

        self._mid_price = mid_price

    @property
    def history(self):
        """Gets the history of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501

        Gets or sets the historical price estimates  # noqa: E501

        :return: The history of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501
        :rtype: list[DomainPublicAdapterWebApiModelsV1PropertiesHistoricalPriceEstimate]
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.

        Gets or sets the historical price estimates  # noqa: E501

        :param history: The history of this DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate.  # noqa: E501
        :type: list[DomainPublicAdapterWebApiModelsV1PropertiesHistoricalPriceEstimate]
        """

        self._history = history

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
        if issubclass(DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate, dict):
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
        if not isinstance(other, DomainPublicAdapterWebApiModelsV1PropertiesPriceEstimate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
