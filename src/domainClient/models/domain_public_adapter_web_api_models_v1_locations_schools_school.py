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


class DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool(object):
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
        'id': 'int',
        'name': 'str',
        'type': 'str',
        'state': 'str',
        'local_government_area': 'str',
        'district': 'str',
        'postcode': 'str',
        'suburb': 'str',
        'street': 'str',
        'display_address': 'str',
        'phone': 'str',
        'fax': 'str',
        'email': 'str',
        'website_url': 'str',
        'crest_url': 'str',
        'education_level': 'str',
        'gender': 'str',
        'low_year': 'str',
        'high_year': 'str',
        'display_year': 'str',
        'geolocation': 'DomainPublicAdapterWebApiModelsV1Point',
        'distance_from_location': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'state': 'state',
        'local_government_area': 'localGovernmentArea',
        'district': 'district',
        'postcode': 'postcode',
        'suburb': 'suburb',
        'street': 'street',
        'display_address': 'displayAddress',
        'phone': 'phone',
        'fax': 'fax',
        'email': 'email',
        'website_url': 'websiteUrl',
        'crest_url': 'crestUrl',
        'education_level': 'educationLevel',
        'gender': 'gender',
        'low_year': 'lowYear',
        'high_year': 'highYear',
        'display_year': 'displayYear',
        'geolocation': 'geolocation',
        'distance_from_location': 'distanceFromLocation'
    }

    def __init__(self, id=None, name=None, type=None, state=None, local_government_area=None, district=None, postcode=None, suburb=None, street=None, display_address=None, phone=None, fax=None, email=None, website_url=None, crest_url=None, education_level=None, gender=None, low_year=None, high_year=None, display_year=None, geolocation=None, distance_from_location=None):  # noqa: E501
        """DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._type = None
        self._state = None
        self._local_government_area = None
        self._district = None
        self._postcode = None
        self._suburb = None
        self._street = None
        self._display_address = None
        self._phone = None
        self._fax = None
        self._email = None
        self._website_url = None
        self._crest_url = None
        self._education_level = None
        self._gender = None
        self._low_year = None
        self._high_year = None
        self._display_year = None
        self._geolocation = None
        self._distance_from_location = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if state is not None:
            self.state = state
        if local_government_area is not None:
            self.local_government_area = local_government_area
        if district is not None:
            self.district = district
        if postcode is not None:
            self.postcode = postcode
        if suburb is not None:
            self.suburb = suburb
        if street is not None:
            self.street = street
        if display_address is not None:
            self.display_address = display_address
        if phone is not None:
            self.phone = phone
        if fax is not None:
            self.fax = fax
        if email is not None:
            self.email = email
        if website_url is not None:
            self.website_url = website_url
        if crest_url is not None:
            self.crest_url = crest_url
        if education_level is not None:
            self.education_level = education_level
        if gender is not None:
            self.gender = gender
        if low_year is not None:
            self.low_year = low_year
        if high_year is not None:
            self.high_year = high_year
        if display_year is not None:
            self.display_year = display_year
        if geolocation is not None:
            self.geolocation = geolocation
        if distance_from_location is not None:
            self.distance_from_location = distance_from_location

    @property
    def id(self):
        """Gets the id of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        School identifier  # noqa: E501

        :return: The id of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        School identifier  # noqa: E501

        :param id: The id of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        School name  # noqa: E501

        :return: The name of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        School name  # noqa: E501

        :param name: The name of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        School type  # noqa: E501

        :return: The type of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        School type  # noqa: E501

        :param type: The type of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def state(self):
        """Gets the state of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        State  # noqa: E501

        :return: The state of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        State  # noqa: E501

        :param state: The state of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def local_government_area(self):
        """Gets the local_government_area of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        Local government area  # noqa: E501

        :return: The local_government_area of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._local_government_area

    @local_government_area.setter
    def local_government_area(self, local_government_area):
        """Sets the local_government_area of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        Local government area  # noqa: E501

        :param local_government_area: The local_government_area of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._local_government_area = local_government_area

    @property
    def district(self):
        """Gets the district of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        District  # noqa: E501

        :return: The district of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """Sets the district of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        District  # noqa: E501

        :param district: The district of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._district = district

    @property
    def postcode(self):
        """Gets the postcode of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        Postcode  # noqa: E501

        :return: The postcode of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        Postcode  # noqa: E501

        :param postcode: The postcode of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

    @property
    def suburb(self):
        """Gets the suburb of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        Suburb  # noqa: E501

        :return: The suburb of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._suburb

    @suburb.setter
    def suburb(self, suburb):
        """Sets the suburb of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        Suburb  # noqa: E501

        :param suburb: The suburb of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._suburb = suburb

    @property
    def street(self):
        """Gets the street of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        Street  # noqa: E501

        :return: The street of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        Street  # noqa: E501

        :param street: The street of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._street = street

    @property
    def display_address(self):
        """Gets the display_address of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        Display address  # noqa: E501

        :return: The display_address of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._display_address

    @display_address.setter
    def display_address(self, display_address):
        """Sets the display_address of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        Display address  # noqa: E501

        :param display_address: The display_address of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._display_address = display_address

    @property
    def phone(self):
        """Gets the phone of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        Phone number  # noqa: E501

        :return: The phone of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        Phone number  # noqa: E501

        :param phone: The phone of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def fax(self):
        """Gets the fax of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        Fax number  # noqa: E501

        :return: The fax of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        Fax number  # noqa: E501

        :param fax: The fax of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def email(self):
        """Gets the email of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        Email  # noqa: E501

        :return: The email of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        Email  # noqa: E501

        :param email: The email of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def website_url(self):
        """Gets the website_url of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        Website  # noqa: E501

        :return: The website_url of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._website_url

    @website_url.setter
    def website_url(self, website_url):
        """Sets the website_url of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        Website  # noqa: E501

        :param website_url: The website_url of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._website_url = website_url

    @property
    def crest_url(self):
        """Gets the crest_url of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        School crest  # noqa: E501

        :return: The crest_url of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._crest_url

    @crest_url.setter
    def crest_url(self, crest_url):
        """Sets the crest_url of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        School crest  # noqa: E501

        :param crest_url: The crest_url of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._crest_url = crest_url

    @property
    def education_level(self):
        """Gets the education_level of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        Education level  # noqa: E501

        :return: The education_level of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._education_level

    @education_level.setter
    def education_level(self, education_level):
        """Sets the education_level of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        Education level  # noqa: E501

        :param education_level: The education_level of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._education_level = education_level

    @property
    def gender(self):
        """Gets the gender of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        Gender  # noqa: E501

        :return: The gender of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        Gender  # noqa: E501

        :param gender: The gender of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def low_year(self):
        """Gets the low_year of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        Lower year  # noqa: E501

        :return: The low_year of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._low_year

    @low_year.setter
    def low_year(self, low_year):
        """Sets the low_year of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        Lower year  # noqa: E501

        :param low_year: The low_year of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._low_year = low_year

    @property
    def high_year(self):
        """Gets the high_year of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        Upper year  # noqa: E501

        :return: The high_year of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._high_year

    @high_year.setter
    def high_year(self, high_year):
        """Sets the high_year of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        Upper year  # noqa: E501

        :param high_year: The high_year of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._high_year = high_year

    @property
    def display_year(self):
        """Gets the display_year of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        Year diplay  # noqa: E501

        :return: The display_year of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: str
        """
        return self._display_year

    @display_year.setter
    def display_year(self, display_year):
        """Sets the display_year of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        Year diplay  # noqa: E501

        :param display_year: The display_year of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: str
        """

        self._display_year = display_year

    @property
    def geolocation(self):
        """Gets the geolocation of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        Coordinate  # noqa: E501

        :return: The geolocation of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: DomainPublicAdapterWebApiModelsV1Point
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation):
        """Sets the geolocation of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        Coordinate  # noqa: E501

        :param geolocation: The geolocation of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: DomainPublicAdapterWebApiModelsV1Point
        """

        self._geolocation = geolocation

    @property
    def distance_from_location(self):
        """Gets the distance_from_location of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501

        Distance from search location in metres  # noqa: E501

        :return: The distance_from_location of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :rtype: float
        """
        return self._distance_from_location

    @distance_from_location.setter
    def distance_from_location(self, distance_from_location):
        """Sets the distance_from_location of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.

        Distance from search location in metres  # noqa: E501

        :param distance_from_location: The distance_from_location of this DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool.  # noqa: E501
        :type: float
        """

        self._distance_from_location = distance_from_location

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
        if issubclass(DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool, dict):
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
        if not isinstance(other, DomainPublicAdapterWebApiModelsV1LocationsSchoolsSchool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other