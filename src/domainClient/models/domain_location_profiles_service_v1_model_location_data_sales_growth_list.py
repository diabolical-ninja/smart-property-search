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


class DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList(object):
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
        'median_sold_price': 'float',
        'annual_growth': 'float',
        'number_sold': 'int',
        'year': 'int'
    }

    attribute_map = {
        'median_sold_price': 'medianSoldPrice',
        'annual_growth': 'annualGrowth',
        'number_sold': 'numberSold',
        'year': 'year'
    }

    def __init__(self, median_sold_price=None, annual_growth=None, number_sold=None, year=None):  # noqa: E501
        """DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList - a model defined in Swagger"""  # noqa: E501

        self._median_sold_price = None
        self._annual_growth = None
        self._number_sold = None
        self._year = None
        self.discriminator = None

        if median_sold_price is not None:
            self.median_sold_price = median_sold_price
        if annual_growth is not None:
            self.annual_growth = annual_growth
        if number_sold is not None:
            self.number_sold = number_sold
        if year is not None:
            self.year = year

    @property
    def median_sold_price(self):
        """Gets the median_sold_price of this DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList.  # noqa: E501


        :return: The median_sold_price of this DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList.  # noqa: E501
        :rtype: float
        """
        return self._median_sold_price

    @median_sold_price.setter
    def median_sold_price(self, median_sold_price):
        """Sets the median_sold_price of this DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList.


        :param median_sold_price: The median_sold_price of this DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList.  # noqa: E501
        :type: float
        """

        self._median_sold_price = median_sold_price

    @property
    def annual_growth(self):
        """Gets the annual_growth of this DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList.  # noqa: E501


        :return: The annual_growth of this DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList.  # noqa: E501
        :rtype: float
        """
        return self._annual_growth

    @annual_growth.setter
    def annual_growth(self, annual_growth):
        """Sets the annual_growth of this DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList.


        :param annual_growth: The annual_growth of this DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList.  # noqa: E501
        :type: float
        """

        self._annual_growth = annual_growth

    @property
    def number_sold(self):
        """Gets the number_sold of this DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList.  # noqa: E501


        :return: The number_sold of this DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList.  # noqa: E501
        :rtype: int
        """
        return self._number_sold

    @number_sold.setter
    def number_sold(self, number_sold):
        """Sets the number_sold of this DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList.


        :param number_sold: The number_sold of this DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList.  # noqa: E501
        :type: int
        """

        self._number_sold = number_sold

    @property
    def year(self):
        """Gets the year of this DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList.  # noqa: E501


        :return: The year of this DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList.


        :param year: The year of this DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList.  # noqa: E501
        :type: int
        """

        self._year = year

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
        if issubclass(DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList, dict):
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
        if not isinstance(other, DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
