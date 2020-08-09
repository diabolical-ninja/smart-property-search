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


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections(object):
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
        'inspections': 'list[DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspection]',
        'past_inspections': 'list[DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspection]',
        'is_by_appointment_only': 'bool'
    }

    attribute_map = {
        'inspections': 'inspections',
        'past_inspections': 'pastInspections',
        'is_by_appointment_only': 'isByAppointmentOnly'
    }

    def __init__(self, inspections=None, past_inspections=None, is_by_appointment_only=None):  # noqa: E501
        """DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections - a model defined in Swagger"""  # noqa: E501

        self._inspections = None
        self._past_inspections = None
        self._is_by_appointment_only = None
        self.discriminator = None

        if inspections is not None:
            self.inspections = inspections
        if past_inspections is not None:
            self.past_inspections = past_inspections
        if is_by_appointment_only is not None:
            self.is_by_appointment_only = is_by_appointment_only

    @property
    def inspections(self):
        """Gets the inspections of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections.  # noqa: E501


        :return: The inspections of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections.  # noqa: E501
        :rtype: list[DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspection]
        """
        return self._inspections

    @inspections.setter
    def inspections(self, inspections):
        """Sets the inspections of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections.


        :param inspections: The inspections of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections.  # noqa: E501
        :type: list[DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspection]
        """

        self._inspections = inspections

    @property
    def past_inspections(self):
        """Gets the past_inspections of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections.  # noqa: E501


        :return: The past_inspections of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections.  # noqa: E501
        :rtype: list[DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspection]
        """
        return self._past_inspections

    @past_inspections.setter
    def past_inspections(self, past_inspections):
        """Sets the past_inspections of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections.


        :param past_inspections: The past_inspections of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections.  # noqa: E501
        :type: list[DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspection]
        """

        self._past_inspections = past_inspections

    @property
    def is_by_appointment_only(self):
        """Gets the is_by_appointment_only of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections.  # noqa: E501


        :return: The is_by_appointment_only of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections.  # noqa: E501
        :rtype: bool
        """
        return self._is_by_appointment_only

    @is_by_appointment_only.setter
    def is_by_appointment_only(self, is_by_appointment_only):
        """Sets the is_by_appointment_only of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections.


        :param is_by_appointment_only: The is_by_appointment_only of this DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections.  # noqa: E501
        :type: bool
        """

        self._is_by_appointment_only = is_by_appointment_only

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
        if issubclass(DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections, dict):
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
        if not isinstance(other, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
