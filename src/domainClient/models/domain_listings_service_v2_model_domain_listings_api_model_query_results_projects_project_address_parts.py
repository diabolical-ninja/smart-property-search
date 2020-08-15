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


class DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts(object):
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
        'state_abbreviation': 'str',
        'display_type': 'str',
        'street2': 'str',
        'latitude': 'float',
        'longitude': 'float',
        'street_number': 'str',
        'unit_number': 'str',
        'street': 'str',
        'suburb': 'str',
        'suburb_id': 'int',
        'postcode': 'str',
        'display_address': 'str'
    }

    attribute_map = {
        'state_abbreviation': 'stateAbbreviation',
        'display_type': 'displayType',
        'street2': 'street2',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'street_number': 'streetNumber',
        'unit_number': 'unitNumber',
        'street': 'street',
        'suburb': 'suburb',
        'suburb_id': 'suburbId',
        'postcode': 'postcode',
        'display_address': 'displayAddress'
    }

    def __init__(self, state_abbreviation=None, display_type=None, street2=None, latitude=None, longitude=None, street_number=None, unit_number=None, street=None, suburb=None, suburb_id=None, postcode=None, display_address=None):  # noqa: E501
        """DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts - a model defined in Swagger"""  # noqa: E501

        self._state_abbreviation = None
        self._display_type = None
        self._street2 = None
        self._latitude = None
        self._longitude = None
        self._street_number = None
        self._unit_number = None
        self._street = None
        self._suburb = None
        self._suburb_id = None
        self._postcode = None
        self._display_address = None
        self.discriminator = None

        if state_abbreviation is not None:
            self.state_abbreviation = state_abbreviation
        if display_type is not None:
            self.display_type = display_type
        if street2 is not None:
            self.street2 = street2
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if street_number is not None:
            self.street_number = street_number
        if unit_number is not None:
            self.unit_number = unit_number
        if street is not None:
            self.street = street
        if suburb is not None:
            self.suburb = suburb
        if suburb_id is not None:
            self.suburb_id = suburb_id
        if postcode is not None:
            self.postcode = postcode
        if display_address is not None:
            self.display_address = display_address

    @property
    def state_abbreviation(self):
        """Gets the state_abbreviation of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501


        :return: The state_abbreviation of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :rtype: str
        """
        return self._state_abbreviation

    @state_abbreviation.setter
    def state_abbreviation(self, state_abbreviation):
        """Sets the state_abbreviation of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.


        :param state_abbreviation: The state_abbreviation of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :type: str
        """
        allowed_values = ["nsw", "vic", "sa", "nt", "tas", "act", "qld", "wa"]  # noqa: E501
        if state_abbreviation not in allowed_values:
            raise ValueError(
                "Invalid value for `state_abbreviation` ({0}), must be one of {1}"  # noqa: E501
                .format(state_abbreviation, allowed_values)
            )

        self._state_abbreviation = state_abbreviation

    @property
    def display_type(self):
        """Gets the display_type of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501


        :return: The display_type of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :rtype: str
        """
        return self._display_type

    @display_type.setter
    def display_type(self, display_type):
        """Sets the display_type of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.


        :param display_type: The display_type of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :type: str
        """
        allowed_values = ["fullAddress", "streetAndSuburb", "suburbOnly", "regionOnly", "areaOnly", "stateOnly"]  # noqa: E501
        if display_type not in allowed_values:
            raise ValueError(
                "Invalid value for `display_type` ({0}), must be one of {1}"  # noqa: E501
                .format(display_type, allowed_values)
            )

        self._display_type = display_type

    @property
    def street2(self):
        """Gets the street2 of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501


        :return: The street2 of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :rtype: str
        """
        return self._street2

    @street2.setter
    def street2(self, street2):
        """Sets the street2 of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.


        :param street2: The street2 of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :type: str
        """

        self._street2 = street2

    @property
    def latitude(self):
        """Gets the latitude of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501


        :return: The latitude of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.


        :param latitude: The latitude of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501


        :return: The longitude of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.


        :param longitude: The longitude of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def street_number(self):
        """Gets the street_number of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501


        :return: The street_number of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :rtype: str
        """
        return self._street_number

    @street_number.setter
    def street_number(self, street_number):
        """Sets the street_number of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.


        :param street_number: The street_number of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :type: str
        """

        self._street_number = street_number

    @property
    def unit_number(self):
        """Gets the unit_number of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501


        :return: The unit_number of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :rtype: str
        """
        return self._unit_number

    @unit_number.setter
    def unit_number(self, unit_number):
        """Sets the unit_number of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.


        :param unit_number: The unit_number of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :type: str
        """

        self._unit_number = unit_number

    @property
    def street(self):
        """Gets the street of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501


        :return: The street of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.


        :param street: The street of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :type: str
        """

        self._street = street

    @property
    def suburb(self):
        """Gets the suburb of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501


        :return: The suburb of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :rtype: str
        """
        return self._suburb

    @suburb.setter
    def suburb(self, suburb):
        """Sets the suburb of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.


        :param suburb: The suburb of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :type: str
        """

        self._suburb = suburb

    @property
    def suburb_id(self):
        """Gets the suburb_id of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501


        :return: The suburb_id of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :rtype: int
        """
        return self._suburb_id

    @suburb_id.setter
    def suburb_id(self, suburb_id):
        """Sets the suburb_id of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.


        :param suburb_id: The suburb_id of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :type: int
        """

        self._suburb_id = suburb_id

    @property
    def postcode(self):
        """Gets the postcode of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501


        :return: The postcode of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.


        :param postcode: The postcode of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

    @property
    def display_address(self):
        """Gets the display_address of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501


        :return: The display_address of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :rtype: str
        """
        return self._display_address

    @display_address.setter
    def display_address(self, display_address):
        """Sets the display_address of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.


        :param display_address: The display_address of this DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts.  # noqa: E501
        :type: str
        """

        self._display_address = display_address

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
        if issubclass(DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts, dict):
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
        if not isinstance(other, DomainListingsServiceV2ModelDomainListingsApiModelQueryResultsProjectsProjectAddressParts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other