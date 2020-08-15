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


class DomainAgencyServiceV2ModelAgency(object):
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
        'account_type': 'str',
        'profile': 'DomainAgencyServiceV2ModelAgencyProfile',
        'date_updated': 'datetime',
        'name': 'str',
        'details': 'DomainAgencyServiceV2ModelAgencyDetails',
        'id': 'int',
        'cre_id': 'int',
        'agents': 'list[DomainAgencyServiceV2ModelAgentInAgencyList]',
        'contact_details': 'DomainAgencyServiceV2ModelContactDetails',
        'homepass_enabled': 'bool',
        'suburbs_served': 'str',
        'subscribed_to_agency_performance_report': 'bool',
        'agency_options': 'DomainAgencyServiceV2ModelAgencyOptions',
        'welcome_message': 'str',
        'ad_format': 'str',
        'provider_agency_id': 'str'
    }

    attribute_map = {
        'account_type': 'accountType',
        'profile': 'profile',
        'date_updated': 'dateUpdated',
        'name': 'name',
        'details': 'details',
        'id': 'id',
        'cre_id': 'creId',
        'agents': 'agents',
        'contact_details': 'contactDetails',
        'homepass_enabled': 'homepassEnabled',
        'suburbs_served': 'suburbsServed',
        'subscribed_to_agency_performance_report': 'subscribedToAgencyPerformanceReport',
        'agency_options': 'agencyOptions',
        'welcome_message': 'welcomeMessage',
        'ad_format': 'adFormat',
        'provider_agency_id': 'providerAgencyId'
    }

    def __init__(self, account_type=None, profile=None, date_updated=None, name=None, details=None, id=None, cre_id=None, agents=None, contact_details=None, homepass_enabled=None, suburbs_served=None, subscribed_to_agency_performance_report=None, agency_options=None, welcome_message=None, ad_format=None, provider_agency_id=None):  # noqa: E501
        """DomainAgencyServiceV2ModelAgency - a model defined in Swagger"""  # noqa: E501

        self._account_type = None
        self._profile = None
        self._date_updated = None
        self._name = None
        self._details = None
        self._id = None
        self._cre_id = None
        self._agents = None
        self._contact_details = None
        self._homepass_enabled = None
        self._suburbs_served = None
        self._subscribed_to_agency_performance_report = None
        self._agency_options = None
        self._welcome_message = None
        self._ad_format = None
        self._provider_agency_id = None
        self.discriminator = None

        if account_type is not None:
            self.account_type = account_type
        if profile is not None:
            self.profile = profile
        if date_updated is not None:
            self.date_updated = date_updated
        if name is not None:
            self.name = name
        if details is not None:
            self.details = details
        if id is not None:
            self.id = id
        if cre_id is not None:
            self.cre_id = cre_id
        if agents is not None:
            self.agents = agents
        if contact_details is not None:
            self.contact_details = contact_details
        if homepass_enabled is not None:
            self.homepass_enabled = homepass_enabled
        if suburbs_served is not None:
            self.suburbs_served = suburbs_served
        if subscribed_to_agency_performance_report is not None:
            self.subscribed_to_agency_performance_report = subscribed_to_agency_performance_report
        if agency_options is not None:
            self.agency_options = agency_options
        if welcome_message is not None:
            self.welcome_message = welcome_message
        if ad_format is not None:
            self.ad_format = ad_format
        if provider_agency_id is not None:
            self.provider_agency_id = provider_agency_id

    @property
    def account_type(self):
        """Gets the account_type of this DomainAgencyServiceV2ModelAgency.  # noqa: E501


        :return: The account_type of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this DomainAgencyServiceV2ModelAgency.


        :param account_type: The account_type of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "residential", "commercialLight", "commercialFull", "developer", "holiday", "business"]  # noqa: E501
        if account_type not in allowed_values:
            raise ValueError(
                "Invalid value for `account_type` ({0}), must be one of {1}"  # noqa: E501
                .format(account_type, allowed_values)
            )

        self._account_type = account_type

    @property
    def profile(self):
        """Gets the profile of this DomainAgencyServiceV2ModelAgency.  # noqa: E501


        :return: The profile of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :rtype: DomainAgencyServiceV2ModelAgencyProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this DomainAgencyServiceV2ModelAgency.


        :param profile: The profile of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :type: DomainAgencyServiceV2ModelAgencyProfile
        """

        self._profile = profile

    @property
    def date_updated(self):
        """Gets the date_updated of this DomainAgencyServiceV2ModelAgency.  # noqa: E501


        :return: The date_updated of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :rtype: datetime
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """Sets the date_updated of this DomainAgencyServiceV2ModelAgency.


        :param date_updated: The date_updated of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :type: datetime
        """

        self._date_updated = date_updated

    @property
    def name(self):
        """Gets the name of this DomainAgencyServiceV2ModelAgency.  # noqa: E501


        :return: The name of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DomainAgencyServiceV2ModelAgency.


        :param name: The name of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def details(self):
        """Gets the details of this DomainAgencyServiceV2ModelAgency.  # noqa: E501


        :return: The details of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :rtype: DomainAgencyServiceV2ModelAgencyDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this DomainAgencyServiceV2ModelAgency.


        :param details: The details of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :type: DomainAgencyServiceV2ModelAgencyDetails
        """

        self._details = details

    @property
    def id(self):
        """Gets the id of this DomainAgencyServiceV2ModelAgency.  # noqa: E501


        :return: The id of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainAgencyServiceV2ModelAgency.


        :param id: The id of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def cre_id(self):
        """Gets the cre_id of this DomainAgencyServiceV2ModelAgency.  # noqa: E501


        :return: The cre_id of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :rtype: int
        """
        return self._cre_id

    @cre_id.setter
    def cre_id(self, cre_id):
        """Sets the cre_id of this DomainAgencyServiceV2ModelAgency.


        :param cre_id: The cre_id of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :type: int
        """

        self._cre_id = cre_id

    @property
    def agents(self):
        """Gets the agents of this DomainAgencyServiceV2ModelAgency.  # noqa: E501


        :return: The agents of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :rtype: list[DomainAgencyServiceV2ModelAgentInAgencyList]
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """Sets the agents of this DomainAgencyServiceV2ModelAgency.


        :param agents: The agents of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :type: list[DomainAgencyServiceV2ModelAgentInAgencyList]
        """

        self._agents = agents

    @property
    def contact_details(self):
        """Gets the contact_details of this DomainAgencyServiceV2ModelAgency.  # noqa: E501


        :return: The contact_details of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :rtype: DomainAgencyServiceV2ModelContactDetails
        """
        return self._contact_details

    @contact_details.setter
    def contact_details(self, contact_details):
        """Sets the contact_details of this DomainAgencyServiceV2ModelAgency.


        :param contact_details: The contact_details of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :type: DomainAgencyServiceV2ModelContactDetails
        """

        self._contact_details = contact_details

    @property
    def homepass_enabled(self):
        """Gets the homepass_enabled of this DomainAgencyServiceV2ModelAgency.  # noqa: E501


        :return: The homepass_enabled of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :rtype: bool
        """
        return self._homepass_enabled

    @homepass_enabled.setter
    def homepass_enabled(self, homepass_enabled):
        """Sets the homepass_enabled of this DomainAgencyServiceV2ModelAgency.


        :param homepass_enabled: The homepass_enabled of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :type: bool
        """

        self._homepass_enabled = homepass_enabled

    @property
    def suburbs_served(self):
        """Gets the suburbs_served of this DomainAgencyServiceV2ModelAgency.  # noqa: E501


        :return: The suburbs_served of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :rtype: str
        """
        return self._suburbs_served

    @suburbs_served.setter
    def suburbs_served(self, suburbs_served):
        """Sets the suburbs_served of this DomainAgencyServiceV2ModelAgency.


        :param suburbs_served: The suburbs_served of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :type: str
        """

        self._suburbs_served = suburbs_served

    @property
    def subscribed_to_agency_performance_report(self):
        """Gets the subscribed_to_agency_performance_report of this DomainAgencyServiceV2ModelAgency.  # noqa: E501


        :return: The subscribed_to_agency_performance_report of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :rtype: bool
        """
        return self._subscribed_to_agency_performance_report

    @subscribed_to_agency_performance_report.setter
    def subscribed_to_agency_performance_report(self, subscribed_to_agency_performance_report):
        """Sets the subscribed_to_agency_performance_report of this DomainAgencyServiceV2ModelAgency.


        :param subscribed_to_agency_performance_report: The subscribed_to_agency_performance_report of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :type: bool
        """

        self._subscribed_to_agency_performance_report = subscribed_to_agency_performance_report

    @property
    def agency_options(self):
        """Gets the agency_options of this DomainAgencyServiceV2ModelAgency.  # noqa: E501


        :return: The agency_options of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :rtype: DomainAgencyServiceV2ModelAgencyOptions
        """
        return self._agency_options

    @agency_options.setter
    def agency_options(self, agency_options):
        """Sets the agency_options of this DomainAgencyServiceV2ModelAgency.


        :param agency_options: The agency_options of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :type: DomainAgencyServiceV2ModelAgencyOptions
        """

        self._agency_options = agency_options

    @property
    def welcome_message(self):
        """Gets the welcome_message of this DomainAgencyServiceV2ModelAgency.  # noqa: E501


        :return: The welcome_message of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :rtype: str
        """
        return self._welcome_message

    @welcome_message.setter
    def welcome_message(self, welcome_message):
        """Sets the welcome_message of this DomainAgencyServiceV2ModelAgency.


        :param welcome_message: The welcome_message of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :type: str
        """

        self._welcome_message = welcome_message

    @property
    def ad_format(self):
        """Gets the ad_format of this DomainAgencyServiceV2ModelAgency.  # noqa: E501


        :return: The ad_format of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :rtype: str
        """
        return self._ad_format

    @ad_format.setter
    def ad_format(self, ad_format):
        """Sets the ad_format of this DomainAgencyServiceV2ModelAgency.


        :param ad_format: The ad_format of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :type: str
        """

        self._ad_format = ad_format

    @property
    def provider_agency_id(self):
        """Gets the provider_agency_id of this DomainAgencyServiceV2ModelAgency.  # noqa: E501


        :return: The provider_agency_id of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :rtype: str
        """
        return self._provider_agency_id

    @provider_agency_id.setter
    def provider_agency_id(self, provider_agency_id):
        """Sets the provider_agency_id of this DomainAgencyServiceV2ModelAgency.


        :param provider_agency_id: The provider_agency_id of this DomainAgencyServiceV2ModelAgency.  # noqa: E501
        :type: str
        """

        self._provider_agency_id = provider_agency_id

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
        if issubclass(DomainAgencyServiceV2ModelAgency, dict):
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
        if not isinstance(other, DomainAgencyServiceV2ModelAgency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other