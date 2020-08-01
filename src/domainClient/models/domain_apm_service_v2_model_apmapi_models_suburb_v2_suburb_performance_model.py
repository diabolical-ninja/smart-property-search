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


class DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SuburbPerformanceModel(object):
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
        'header': 'DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SeriesHeaderModel',
        'series': 'DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SeriesModel'
    }

    attribute_map = {
        'header': 'header',
        'series': 'series'
    }

    def __init__(self, header=None, series=None):  # noqa: E501
        """DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SuburbPerformanceModel - a model defined in Swagger"""  # noqa: E501

        self._header = None
        self._series = None
        self.discriminator = None

        if header is not None:
            self.header = header
        if series is not None:
            self.series = series

    @property
    def header(self):
        """Gets the header of this DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SuburbPerformanceModel.  # noqa: E501


        :return: The header of this DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SuburbPerformanceModel.  # noqa: E501
        :rtype: DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SeriesHeaderModel
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SuburbPerformanceModel.


        :param header: The header of this DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SuburbPerformanceModel.  # noqa: E501
        :type: DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SeriesHeaderModel
        """

        self._header = header

    @property
    def series(self):
        """Gets the series of this DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SuburbPerformanceModel.  # noqa: E501


        :return: The series of this DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SuburbPerformanceModel.  # noqa: E501
        :rtype: DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SeriesModel
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SuburbPerformanceModel.


        :param series: The series of this DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SuburbPerformanceModel.  # noqa: E501
        :type: DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SeriesModel
        """

        self._series = series

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
        if issubclass(DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SuburbPerformanceModel, dict):
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
        if not isinstance(other, DomainAPMServiceV2ModelAPMAPIModelsSuburbV2SuburbPerformanceModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
