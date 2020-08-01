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


class DomainPublicAdapterWebApiModelsV1ProductsRateForNewListingModel(object):
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
        'cost_ex_gst': 'float',
        'contract_end_date': 'datetime'
    }

    attribute_map = {
        'cost_ex_gst': 'costExGst',
        'contract_end_date': 'contractEndDate'
    }

    def __init__(self, cost_ex_gst=None, contract_end_date=None):  # noqa: E501
        """DomainPublicAdapterWebApiModelsV1ProductsRateForNewListingModel - a model defined in Swagger"""  # noqa: E501

        self._cost_ex_gst = None
        self._contract_end_date = None
        self.discriminator = None

        if cost_ex_gst is not None:
            self.cost_ex_gst = cost_ex_gst
        if contract_end_date is not None:
            self.contract_end_date = contract_end_date

    @property
    def cost_ex_gst(self):
        """Gets the cost_ex_gst of this DomainPublicAdapterWebApiModelsV1ProductsRateForNewListingModel.  # noqa: E501

          # noqa: E501

        :return: The cost_ex_gst of this DomainPublicAdapterWebApiModelsV1ProductsRateForNewListingModel.  # noqa: E501
        :rtype: float
        """
        return self._cost_ex_gst

    @cost_ex_gst.setter
    def cost_ex_gst(self, cost_ex_gst):
        """Sets the cost_ex_gst of this DomainPublicAdapterWebApiModelsV1ProductsRateForNewListingModel.

          # noqa: E501

        :param cost_ex_gst: The cost_ex_gst of this DomainPublicAdapterWebApiModelsV1ProductsRateForNewListingModel.  # noqa: E501
        :type: float
        """

        self._cost_ex_gst = cost_ex_gst

    @property
    def contract_end_date(self):
        """Gets the contract_end_date of this DomainPublicAdapterWebApiModelsV1ProductsRateForNewListingModel.  # noqa: E501

          # noqa: E501

        :return: The contract_end_date of this DomainPublicAdapterWebApiModelsV1ProductsRateForNewListingModel.  # noqa: E501
        :rtype: datetime
        """
        return self._contract_end_date

    @contract_end_date.setter
    def contract_end_date(self, contract_end_date):
        """Sets the contract_end_date of this DomainPublicAdapterWebApiModelsV1ProductsRateForNewListingModel.

          # noqa: E501

        :param contract_end_date: The contract_end_date of this DomainPublicAdapterWebApiModelsV1ProductsRateForNewListingModel.  # noqa: E501
        :type: datetime
        """

        self._contract_end_date = contract_end_date

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
        if issubclass(DomainPublicAdapterWebApiModelsV1ProductsRateForNewListingModel, dict):
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
        if not isinstance(other, DomainPublicAdapterWebApiModelsV1ProductsRateForNewListingModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
