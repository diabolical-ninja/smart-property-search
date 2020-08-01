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


class DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch(object):
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
        'area': 'str',
        'postcode': 'str',
        'region': 'str',
        'state': 'str',
        'street': 'str',
        'suburb': 'str'
    }

    attribute_map = {
        'area': 'area',
        'postcode': 'postcode',
        'region': 'region',
        'state': 'state',
        'street': 'street',
        'suburb': 'suburb'
    }

    def __init__(self, area=None, postcode=None, region=None, state=None, street=None, suburb=None):  # noqa: E501
        """DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch - a model defined in Swagger"""  # noqa: E501

        self._area = None
        self._postcode = None
        self._region = None
        self._state = None
        self._street = None
        self._suburb = None
        self.discriminator = None

        if area is not None:
            self.area = area
        if postcode is not None:
            self.postcode = postcode
        if region is not None:
            self.region = region
        if state is not None:
            self.state = state
        if street is not None:
            self.street = street
        if suburb is not None:
            self.suburb = suburb

    @property
    def area(self):
        """Gets the area of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501

        Location area  # noqa: E501

        :return: The area of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.

        Location area  # noqa: E501

        :param area: The area of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501
        :type: str
        """

        self._area = area

    @property
    def postcode(self):
        """Gets the postcode of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501

        Location postcode  # noqa: E501

        :return: The postcode of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.

        Location postcode  # noqa: E501

        :param postcode: The postcode of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

    @property
    def region(self):
        """Gets the region of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501

        Location region  # noqa: E501

        :return: The region of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.

        Location region  # noqa: E501

        :param region: The region of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def state(self):
        """Gets the state of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501

        State  # noqa: E501

        :return: The state of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.

        State  # noqa: E501

        :param state: The state of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501
        :type: str
        """
        allowed_values = ["act", "nsw", "qld", "vic", "sa", "wa", "nt", "tas"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def street(self):
        """Gets the street of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501

        Street address  # noqa: E501

        :return: The street of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.

        Street address  # noqa: E501

        :param street: The street of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501
        :type: str
        """

        self._street = street

    @property
    def suburb(self):
        """Gets the suburb of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501

        Suburb  # noqa: E501

        :return: The suburb of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501
        :rtype: str
        """
        return self._suburb

    @suburb.setter
    def suburb(self, suburb):
        """Sets the suburb of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.

        Suburb  # noqa: E501

        :param suburb: The suburb of this DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch.  # noqa: E501
        :type: str
        """

        self._suburb = suburb

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
        if issubclass(DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch, dict):
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
        if not isinstance(other, DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
