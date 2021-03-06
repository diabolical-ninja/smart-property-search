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


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails(object):
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
        'sold_action': 'str',
        'source': 'str',
        'sold_price': 'int',
        'government_recorded_sold_price': 'int',
        'sold_date': 'datetime',
        'can_display_price': 'bool'
    }

    attribute_map = {
        'sold_action': 'soldAction',
        'source': 'source',
        'sold_price': 'soldPrice',
        'government_recorded_sold_price': 'governmentRecordedSoldPrice',
        'sold_date': 'soldDate',
        'can_display_price': 'canDisplayPrice'
    }

    def __init__(self, sold_action=None, source=None, sold_price=None, government_recorded_sold_price=None, sold_date=None, can_display_price=None):  # noqa: E501
        """DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails - a model defined in Swagger"""  # noqa: E501

        self._sold_action = None
        self._source = None
        self._sold_price = None
        self._government_recorded_sold_price = None
        self._sold_date = None
        self._can_display_price = None
        self.discriminator = None

        if sold_action is not None:
            self.sold_action = sold_action
        if source is not None:
            self.source = source
        if sold_price is not None:
            self.sold_price = sold_price
        if government_recorded_sold_price is not None:
            self.government_recorded_sold_price = government_recorded_sold_price
        if sold_date is not None:
            self.sold_date = sold_date
        if can_display_price is not None:
            self.can_display_price = can_display_price

    @property
    def sold_action(self):
        """Gets the sold_action of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501


        :return: The sold_action of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501
        :rtype: str
        """
        return self._sold_action

    @sold_action.setter
    def sold_action(self, sold_action):
        """Sets the sold_action of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.


        :param sold_action: The sold_action of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["notStated", "auction", "privateTreaty", "withdrawn", "soldPriorToAuction"]  # noqa: E501
        if sold_action not in allowed_values:
            raise ValueError(
                "Invalid value for `sold_action` ({0}), must be one of {1}"  # noqa: E501
                .format(sold_action, allowed_values)
            )

        self._sold_action = sold_action

    @property
    def source(self):
        """Gets the source of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501


        :return: The source of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.


        :param source: The source of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["internal", "external"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def sold_price(self):
        """Gets the sold_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501


        :return: The sold_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501
        :rtype: int
        """
        return self._sold_price

    @sold_price.setter
    def sold_price(self, sold_price):
        """Sets the sold_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.


        :param sold_price: The sold_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501
        :type: int
        """

        self._sold_price = sold_price

    @property
    def government_recorded_sold_price(self):
        """Gets the government_recorded_sold_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501


        :return: The government_recorded_sold_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501
        :rtype: int
        """
        return self._government_recorded_sold_price

    @government_recorded_sold_price.setter
    def government_recorded_sold_price(self, government_recorded_sold_price):
        """Sets the government_recorded_sold_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.


        :param government_recorded_sold_price: The government_recorded_sold_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501
        :type: int
        """

        self._government_recorded_sold_price = government_recorded_sold_price

    @property
    def sold_date(self):
        """Gets the sold_date of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501


        :return: The sold_date of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._sold_date

    @sold_date.setter
    def sold_date(self, sold_date):
        """Sets the sold_date of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.


        :param sold_date: The sold_date of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501
        :type: datetime
        """

        self._sold_date = sold_date

    @property
    def can_display_price(self):
        """Gets the can_display_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501


        :return: The can_display_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501
        :rtype: bool
        """
        return self._can_display_price

    @can_display_price.setter
    def can_display_price(self, can_display_price):
        """Sets the can_display_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.


        :param can_display_price: The can_display_price of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails.  # noqa: E501
        :type: bool
        """

        self._can_display_price = can_display_price

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
        if issubclass(DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails, dict):
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
        if not isinstance(other, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
