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


class DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary(object):
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
        'number_listed_for_auction': 'int',
        'number_withdrawn': 'int',
        'number_unreported': 'int',
        'number_auctioned': 'int',
        'number_sold': 'int',
        'total_sales': 'float',
        'median': 'int',
        'adj_clearance_rate': 'float',
        'auctioned_date': 'datetime',
        'last_modified_date_time': 'datetime'
    }

    attribute_map = {
        'number_listed_for_auction': 'numberListedForAuction',
        'number_withdrawn': 'numberWithdrawn',
        'number_unreported': 'numberUnreported',
        'number_auctioned': 'numberAuctioned',
        'number_sold': 'numberSold',
        'total_sales': 'totalSales',
        'median': 'median',
        'adj_clearance_rate': 'adjClearanceRate',
        'auctioned_date': 'auctionedDate',
        'last_modified_date_time': 'lastModifiedDateTime'
    }

    def __init__(self, number_listed_for_auction=None, number_withdrawn=None, number_unreported=None, number_auctioned=None, number_sold=None, total_sales=None, median=None, adj_clearance_rate=None, auctioned_date=None, last_modified_date_time=None):  # noqa: E501
        """DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary - a model defined in Swagger"""  # noqa: E501

        self._number_listed_for_auction = None
        self._number_withdrawn = None
        self._number_unreported = None
        self._number_auctioned = None
        self._number_sold = None
        self._total_sales = None
        self._median = None
        self._adj_clearance_rate = None
        self._auctioned_date = None
        self._last_modified_date_time = None
        self.discriminator = None

        if number_listed_for_auction is not None:
            self.number_listed_for_auction = number_listed_for_auction
        if number_withdrawn is not None:
            self.number_withdrawn = number_withdrawn
        if number_unreported is not None:
            self.number_unreported = number_unreported
        if number_auctioned is not None:
            self.number_auctioned = number_auctioned
        if number_sold is not None:
            self.number_sold = number_sold
        if total_sales is not None:
            self.total_sales = total_sales
        if median is not None:
            self.median = median
        if adj_clearance_rate is not None:
            self.adj_clearance_rate = adj_clearance_rate
        if auctioned_date is not None:
            self.auctioned_date = auctioned_date
        if last_modified_date_time is not None:
            self.last_modified_date_time = last_modified_date_time

    @property
    def number_listed_for_auction(self):
        """Gets the number_listed_for_auction of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501


        :return: The number_listed_for_auction of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :rtype: int
        """
        return self._number_listed_for_auction

    @number_listed_for_auction.setter
    def number_listed_for_auction(self, number_listed_for_auction):
        """Sets the number_listed_for_auction of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.


        :param number_listed_for_auction: The number_listed_for_auction of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :type: int
        """

        self._number_listed_for_auction = number_listed_for_auction

    @property
    def number_withdrawn(self):
        """Gets the number_withdrawn of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501


        :return: The number_withdrawn of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :rtype: int
        """
        return self._number_withdrawn

    @number_withdrawn.setter
    def number_withdrawn(self, number_withdrawn):
        """Sets the number_withdrawn of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.


        :param number_withdrawn: The number_withdrawn of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :type: int
        """

        self._number_withdrawn = number_withdrawn

    @property
    def number_unreported(self):
        """Gets the number_unreported of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501


        :return: The number_unreported of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :rtype: int
        """
        return self._number_unreported

    @number_unreported.setter
    def number_unreported(self, number_unreported):
        """Sets the number_unreported of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.


        :param number_unreported: The number_unreported of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :type: int
        """

        self._number_unreported = number_unreported

    @property
    def number_auctioned(self):
        """Gets the number_auctioned of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501


        :return: The number_auctioned of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :rtype: int
        """
        return self._number_auctioned

    @number_auctioned.setter
    def number_auctioned(self, number_auctioned):
        """Sets the number_auctioned of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.


        :param number_auctioned: The number_auctioned of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :type: int
        """

        self._number_auctioned = number_auctioned

    @property
    def number_sold(self):
        """Gets the number_sold of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501


        :return: The number_sold of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :rtype: int
        """
        return self._number_sold

    @number_sold.setter
    def number_sold(self, number_sold):
        """Sets the number_sold of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.


        :param number_sold: The number_sold of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :type: int
        """

        self._number_sold = number_sold

    @property
    def total_sales(self):
        """Gets the total_sales of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501


        :return: The total_sales of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :rtype: float
        """
        return self._total_sales

    @total_sales.setter
    def total_sales(self, total_sales):
        """Sets the total_sales of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.


        :param total_sales: The total_sales of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :type: float
        """

        self._total_sales = total_sales

    @property
    def median(self):
        """Gets the median of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501


        :return: The median of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :rtype: int
        """
        return self._median

    @median.setter
    def median(self, median):
        """Sets the median of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.


        :param median: The median of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :type: int
        """

        self._median = median

    @property
    def adj_clearance_rate(self):
        """Gets the adj_clearance_rate of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501


        :return: The adj_clearance_rate of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :rtype: float
        """
        return self._adj_clearance_rate

    @adj_clearance_rate.setter
    def adj_clearance_rate(self, adj_clearance_rate):
        """Sets the adj_clearance_rate of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.


        :param adj_clearance_rate: The adj_clearance_rate of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :type: float
        """

        self._adj_clearance_rate = adj_clearance_rate

    @property
    def auctioned_date(self):
        """Gets the auctioned_date of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501


        :return: The auctioned_date of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._auctioned_date

    @auctioned_date.setter
    def auctioned_date(self, auctioned_date):
        """Sets the auctioned_date of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.


        :param auctioned_date: The auctioned_date of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :type: datetime
        """

        self._auctioned_date = auctioned_date

    @property
    def last_modified_date_time(self):
        """Gets the last_modified_date_time of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501


        :return: The last_modified_date_time of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date_time

    @last_modified_date_time.setter
    def last_modified_date_time(self, last_modified_date_time):
        """Sets the last_modified_date_time of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.


        :param last_modified_date_time: The last_modified_date_time of this DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary.  # noqa: E501
        :type: datetime
        """

        self._last_modified_date_time = last_modified_date_time

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
        if issubclass(DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary, dict):
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
        if not isinstance(other, DomainSalesResultsServiceV1ModelDomainSalesResultsModelCityResultsSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
