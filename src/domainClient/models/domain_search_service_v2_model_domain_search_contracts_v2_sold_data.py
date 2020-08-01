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


class DomainSearchServiceV2ModelDomainSearchContractsV2SoldData(object):
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
        'source': 'str',
        'sale_method': 'str',
        'sold_date': 'datetime',
        'sold_price': 'int'
    }

    attribute_map = {
        'source': 'source',
        'sale_method': 'saleMethod',
        'sold_date': 'soldDate',
        'sold_price': 'soldPrice'
    }

    def __init__(self, source=None, sale_method=None, sold_date=None, sold_price=None):  # noqa: E501
        """DomainSearchServiceV2ModelDomainSearchContractsV2SoldData - a model defined in Swagger"""  # noqa: E501

        self._source = None
        self._sale_method = None
        self._sold_date = None
        self._sold_price = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if sale_method is not None:
            self.sale_method = sale_method
        if sold_date is not None:
            self.sold_date = sold_date
        if sold_price is not None:
            self.sold_price = sold_price

    @property
    def source(self):
        """Gets the source of this DomainSearchServiceV2ModelDomainSearchContractsV2SoldData.  # noqa: E501


        :return: The source of this DomainSearchServiceV2ModelDomainSearchContractsV2SoldData.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DomainSearchServiceV2ModelDomainSearchContractsV2SoldData.


        :param source: The source of this DomainSearchServiceV2ModelDomainSearchContractsV2SoldData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Agency", "Apm"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def sale_method(self):
        """Gets the sale_method of this DomainSearchServiceV2ModelDomainSearchContractsV2SoldData.  # noqa: E501


        :return: The sale_method of this DomainSearchServiceV2ModelDomainSearchContractsV2SoldData.  # noqa: E501
        :rtype: str
        """
        return self._sale_method

    @sale_method.setter
    def sale_method(self, sale_method):
        """Sets the sale_method of this DomainSearchServiceV2ModelDomainSearchContractsV2SoldData.


        :param sale_method: The sale_method of this DomainSearchServiceV2ModelDomainSearchContractsV2SoldData.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotStated", "SoldByAuction", "SoldByPrivateTreaty", "Withdrawn", "SoldPriorToAuction"]  # noqa: E501
        if sale_method not in allowed_values:
            raise ValueError(
                "Invalid value for `sale_method` ({0}), must be one of {1}"  # noqa: E501
                .format(sale_method, allowed_values)
            )

        self._sale_method = sale_method

    @property
    def sold_date(self):
        """Gets the sold_date of this DomainSearchServiceV2ModelDomainSearchContractsV2SoldData.  # noqa: E501


        :return: The sold_date of this DomainSearchServiceV2ModelDomainSearchContractsV2SoldData.  # noqa: E501
        :rtype: datetime
        """
        return self._sold_date

    @sold_date.setter
    def sold_date(self, sold_date):
        """Sets the sold_date of this DomainSearchServiceV2ModelDomainSearchContractsV2SoldData.


        :param sold_date: The sold_date of this DomainSearchServiceV2ModelDomainSearchContractsV2SoldData.  # noqa: E501
        :type: datetime
        """

        self._sold_date = sold_date

    @property
    def sold_price(self):
        """Gets the sold_price of this DomainSearchServiceV2ModelDomainSearchContractsV2SoldData.  # noqa: E501


        :return: The sold_price of this DomainSearchServiceV2ModelDomainSearchContractsV2SoldData.  # noqa: E501
        :rtype: int
        """
        return self._sold_price

    @sold_price.setter
    def sold_price(self, sold_price):
        """Sets the sold_price of this DomainSearchServiceV2ModelDomainSearchContractsV2SoldData.


        :param sold_price: The sold_price of this DomainSearchServiceV2ModelDomainSearchContractsV2SoldData.  # noqa: E501
        :type: int
        """

        self._sold_price = sold_price

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
        if issubclass(DomainSearchServiceV2ModelDomainSearchContractsV2SoldData, dict):
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
        if not isinstance(other, DomainSearchServiceV2ModelDomainSearchContractsV2SoldData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
