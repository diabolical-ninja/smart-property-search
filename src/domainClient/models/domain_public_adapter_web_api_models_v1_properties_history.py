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


class DomainPublicAdapterWebApiModelsV1PropertiesHistory(object):
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
        'rentals': 'list[DomainPublicAdapterWebApiModelsV1PropertiesRentalActivity]',
        'sales': 'list[DomainPublicAdapterWebApiModelsV1PropertiesSaleActivity]',
        'suppress': 'bool'
    }

    attribute_map = {
        'rentals': 'rentals',
        'sales': 'sales',
        'suppress': 'suppress'
    }

    def __init__(self, rentals=None, sales=None, suppress=None):  # noqa: E501
        """DomainPublicAdapterWebApiModelsV1PropertiesHistory - a model defined in Swagger"""  # noqa: E501

        self._rentals = None
        self._sales = None
        self._suppress = None
        self.discriminator = None

        if rentals is not None:
            self.rentals = rentals
        if sales is not None:
            self.sales = sales
        if suppress is not None:
            self.suppress = suppress

    @property
    def rentals(self):
        """Gets the rentals of this DomainPublicAdapterWebApiModelsV1PropertiesHistory.  # noqa: E501

        The collection of historical rentals.  # noqa: E501

        :return: The rentals of this DomainPublicAdapterWebApiModelsV1PropertiesHistory.  # noqa: E501
        :rtype: list[DomainPublicAdapterWebApiModelsV1PropertiesRentalActivity]
        """
        return self._rentals

    @rentals.setter
    def rentals(self, rentals):
        """Sets the rentals of this DomainPublicAdapterWebApiModelsV1PropertiesHistory.

        The collection of historical rentals.  # noqa: E501

        :param rentals: The rentals of this DomainPublicAdapterWebApiModelsV1PropertiesHistory.  # noqa: E501
        :type: list[DomainPublicAdapterWebApiModelsV1PropertiesRentalActivity]
        """

        self._rentals = rentals

    @property
    def sales(self):
        """Gets the sales of this DomainPublicAdapterWebApiModelsV1PropertiesHistory.  # noqa: E501

        The collection of historical sales.  # noqa: E501

        :return: The sales of this DomainPublicAdapterWebApiModelsV1PropertiesHistory.  # noqa: E501
        :rtype: list[DomainPublicAdapterWebApiModelsV1PropertiesSaleActivity]
        """
        return self._sales

    @sales.setter
    def sales(self, sales):
        """Sets the sales of this DomainPublicAdapterWebApiModelsV1PropertiesHistory.

        The collection of historical sales.  # noqa: E501

        :param sales: The sales of this DomainPublicAdapterWebApiModelsV1PropertiesHistory.  # noqa: E501
        :type: list[DomainPublicAdapterWebApiModelsV1PropertiesSaleActivity]
        """

        self._sales = sales

    @property
    def suppress(self):
        """Gets the suppress of this DomainPublicAdapterWebApiModelsV1PropertiesHistory.  # noqa: E501

        Gets or sets a value indicating whether this {Domain.PropertyId.Model.Models.History} is suppress.  # noqa: E501

        :return: The suppress of this DomainPublicAdapterWebApiModelsV1PropertiesHistory.  # noqa: E501
        :rtype: bool
        """
        return self._suppress

    @suppress.setter
    def suppress(self, suppress):
        """Sets the suppress of this DomainPublicAdapterWebApiModelsV1PropertiesHistory.

        Gets or sets a value indicating whether this {Domain.PropertyId.Model.Models.History} is suppress.  # noqa: E501

        :param suppress: The suppress of this DomainPublicAdapterWebApiModelsV1PropertiesHistory.  # noqa: E501
        :type: bool
        """

        self._suppress = suppress

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
        if issubclass(DomainPublicAdapterWebApiModelsV1PropertiesHistory, dict):
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
        if not isinstance(other, DomainPublicAdapterWebApiModelsV1PropertiesHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
