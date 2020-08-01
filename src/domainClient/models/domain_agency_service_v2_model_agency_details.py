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


class DomainAgencyServiceV2ModelAgencyDetails(object):
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
        'street_address1': 'str',
        'street_address2': 'str',
        'suburb': 'str',
        'state': 'str',
        'postcode': 'str',
        'agency_website': 'str',
        'principal_name': 'str',
        'principal_email': 'str',
        'show_past_sales_prices': 'bool',
        'is_agency_report_enabled': 'bool',
        'sales_email': 'str',
        'rental_email': 'str',
        'is_promotional_telephone_active': 'bool',
        'hide_market_price_estimate': 'bool',
        'limit_email_domain': 'bool',
        'show_tab_sold_last_year': 'bool'
    }

    attribute_map = {
        'street_address1': 'streetAddress1',
        'street_address2': 'streetAddress2',
        'suburb': 'suburb',
        'state': 'state',
        'postcode': 'postcode',
        'agency_website': 'agencyWebsite',
        'principal_name': 'principalName',
        'principal_email': 'principalEmail',
        'show_past_sales_prices': 'showPastSalesPrices',
        'is_agency_report_enabled': 'isAgencyReportEnabled',
        'sales_email': 'salesEmail',
        'rental_email': 'rentalEmail',
        'is_promotional_telephone_active': 'isPromotionalTelephoneActive',
        'hide_market_price_estimate': 'hideMarketPriceEstimate',
        'limit_email_domain': 'limitEmailDomain',
        'show_tab_sold_last_year': 'showTabSoldLastYear'
    }

    def __init__(self, street_address1=None, street_address2=None, suburb=None, state=None, postcode=None, agency_website=None, principal_name=None, principal_email=None, show_past_sales_prices=None, is_agency_report_enabled=None, sales_email=None, rental_email=None, is_promotional_telephone_active=None, hide_market_price_estimate=None, limit_email_domain=None, show_tab_sold_last_year=None):  # noqa: E501
        """DomainAgencyServiceV2ModelAgencyDetails - a model defined in Swagger"""  # noqa: E501

        self._street_address1 = None
        self._street_address2 = None
        self._suburb = None
        self._state = None
        self._postcode = None
        self._agency_website = None
        self._principal_name = None
        self._principal_email = None
        self._show_past_sales_prices = None
        self._is_agency_report_enabled = None
        self._sales_email = None
        self._rental_email = None
        self._is_promotional_telephone_active = None
        self._hide_market_price_estimate = None
        self._limit_email_domain = None
        self._show_tab_sold_last_year = None
        self.discriminator = None

        if street_address1 is not None:
            self.street_address1 = street_address1
        if street_address2 is not None:
            self.street_address2 = street_address2
        if suburb is not None:
            self.suburb = suburb
        if state is not None:
            self.state = state
        if postcode is not None:
            self.postcode = postcode
        if agency_website is not None:
            self.agency_website = agency_website
        if principal_name is not None:
            self.principal_name = principal_name
        if principal_email is not None:
            self.principal_email = principal_email
        if show_past_sales_prices is not None:
            self.show_past_sales_prices = show_past_sales_prices
        if is_agency_report_enabled is not None:
            self.is_agency_report_enabled = is_agency_report_enabled
        if sales_email is not None:
            self.sales_email = sales_email
        if rental_email is not None:
            self.rental_email = rental_email
        if is_promotional_telephone_active is not None:
            self.is_promotional_telephone_active = is_promotional_telephone_active
        if hide_market_price_estimate is not None:
            self.hide_market_price_estimate = hide_market_price_estimate
        if limit_email_domain is not None:
            self.limit_email_domain = limit_email_domain
        if show_tab_sold_last_year is not None:
            self.show_tab_sold_last_year = show_tab_sold_last_year

    @property
    def street_address1(self):
        """Gets the street_address1 of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501


        :return: The street_address1 of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :rtype: str
        """
        return self._street_address1

    @street_address1.setter
    def street_address1(self, street_address1):
        """Sets the street_address1 of this DomainAgencyServiceV2ModelAgencyDetails.


        :param street_address1: The street_address1 of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :type: str
        """

        self._street_address1 = street_address1

    @property
    def street_address2(self):
        """Gets the street_address2 of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501


        :return: The street_address2 of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :rtype: str
        """
        return self._street_address2

    @street_address2.setter
    def street_address2(self, street_address2):
        """Sets the street_address2 of this DomainAgencyServiceV2ModelAgencyDetails.


        :param street_address2: The street_address2 of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :type: str
        """

        self._street_address2 = street_address2

    @property
    def suburb(self):
        """Gets the suburb of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501


        :return: The suburb of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :rtype: str
        """
        return self._suburb

    @suburb.setter
    def suburb(self, suburb):
        """Sets the suburb of this DomainAgencyServiceV2ModelAgencyDetails.


        :param suburb: The suburb of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :type: str
        """

        self._suburb = suburb

    @property
    def state(self):
        """Gets the state of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501


        :return: The state of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DomainAgencyServiceV2ModelAgencyDetails.


        :param state: The state of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def postcode(self):
        """Gets the postcode of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501


        :return: The postcode of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this DomainAgencyServiceV2ModelAgencyDetails.


        :param postcode: The postcode of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

    @property
    def agency_website(self):
        """Gets the agency_website of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501


        :return: The agency_website of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :rtype: str
        """
        return self._agency_website

    @agency_website.setter
    def agency_website(self, agency_website):
        """Sets the agency_website of this DomainAgencyServiceV2ModelAgencyDetails.


        :param agency_website: The agency_website of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :type: str
        """

        self._agency_website = agency_website

    @property
    def principal_name(self):
        """Gets the principal_name of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501


        :return: The principal_name of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :rtype: str
        """
        return self._principal_name

    @principal_name.setter
    def principal_name(self, principal_name):
        """Sets the principal_name of this DomainAgencyServiceV2ModelAgencyDetails.


        :param principal_name: The principal_name of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :type: str
        """

        self._principal_name = principal_name

    @property
    def principal_email(self):
        """Gets the principal_email of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501


        :return: The principal_email of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :rtype: str
        """
        return self._principal_email

    @principal_email.setter
    def principal_email(self, principal_email):
        """Sets the principal_email of this DomainAgencyServiceV2ModelAgencyDetails.


        :param principal_email: The principal_email of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :type: str
        """

        self._principal_email = principal_email

    @property
    def show_past_sales_prices(self):
        """Gets the show_past_sales_prices of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501


        :return: The show_past_sales_prices of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :rtype: bool
        """
        return self._show_past_sales_prices

    @show_past_sales_prices.setter
    def show_past_sales_prices(self, show_past_sales_prices):
        """Sets the show_past_sales_prices of this DomainAgencyServiceV2ModelAgencyDetails.


        :param show_past_sales_prices: The show_past_sales_prices of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :type: bool
        """

        self._show_past_sales_prices = show_past_sales_prices

    @property
    def is_agency_report_enabled(self):
        """Gets the is_agency_report_enabled of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501


        :return: The is_agency_report_enabled of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_agency_report_enabled

    @is_agency_report_enabled.setter
    def is_agency_report_enabled(self, is_agency_report_enabled):
        """Sets the is_agency_report_enabled of this DomainAgencyServiceV2ModelAgencyDetails.


        :param is_agency_report_enabled: The is_agency_report_enabled of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :type: bool
        """

        self._is_agency_report_enabled = is_agency_report_enabled

    @property
    def sales_email(self):
        """Gets the sales_email of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501


        :return: The sales_email of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :rtype: str
        """
        return self._sales_email

    @sales_email.setter
    def sales_email(self, sales_email):
        """Sets the sales_email of this DomainAgencyServiceV2ModelAgencyDetails.


        :param sales_email: The sales_email of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :type: str
        """

        self._sales_email = sales_email

    @property
    def rental_email(self):
        """Gets the rental_email of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501


        :return: The rental_email of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :rtype: str
        """
        return self._rental_email

    @rental_email.setter
    def rental_email(self, rental_email):
        """Sets the rental_email of this DomainAgencyServiceV2ModelAgencyDetails.


        :param rental_email: The rental_email of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :type: str
        """

        self._rental_email = rental_email

    @property
    def is_promotional_telephone_active(self):
        """Gets the is_promotional_telephone_active of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501


        :return: The is_promotional_telephone_active of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_promotional_telephone_active

    @is_promotional_telephone_active.setter
    def is_promotional_telephone_active(self, is_promotional_telephone_active):
        """Sets the is_promotional_telephone_active of this DomainAgencyServiceV2ModelAgencyDetails.


        :param is_promotional_telephone_active: The is_promotional_telephone_active of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :type: bool
        """

        self._is_promotional_telephone_active = is_promotional_telephone_active

    @property
    def hide_market_price_estimate(self):
        """Gets the hide_market_price_estimate of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501


        :return: The hide_market_price_estimate of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :rtype: bool
        """
        return self._hide_market_price_estimate

    @hide_market_price_estimate.setter
    def hide_market_price_estimate(self, hide_market_price_estimate):
        """Sets the hide_market_price_estimate of this DomainAgencyServiceV2ModelAgencyDetails.


        :param hide_market_price_estimate: The hide_market_price_estimate of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :type: bool
        """

        self._hide_market_price_estimate = hide_market_price_estimate

    @property
    def limit_email_domain(self):
        """Gets the limit_email_domain of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501


        :return: The limit_email_domain of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :rtype: bool
        """
        return self._limit_email_domain

    @limit_email_domain.setter
    def limit_email_domain(self, limit_email_domain):
        """Sets the limit_email_domain of this DomainAgencyServiceV2ModelAgencyDetails.


        :param limit_email_domain: The limit_email_domain of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :type: bool
        """

        self._limit_email_domain = limit_email_domain

    @property
    def show_tab_sold_last_year(self):
        """Gets the show_tab_sold_last_year of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501


        :return: The show_tab_sold_last_year of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :rtype: bool
        """
        return self._show_tab_sold_last_year

    @show_tab_sold_last_year.setter
    def show_tab_sold_last_year(self, show_tab_sold_last_year):
        """Sets the show_tab_sold_last_year of this DomainAgencyServiceV2ModelAgencyDetails.


        :param show_tab_sold_last_year: The show_tab_sold_last_year of this DomainAgencyServiceV2ModelAgencyDetails.  # noqa: E501
        :type: bool
        """

        self._show_tab_sold_last_year = show_tab_sold_last_year

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
        if issubclass(DomainAgencyServiceV2ModelAgencyDetails, dict):
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
        if not isinstance(other, DomainAgencyServiceV2ModelAgencyDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
