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


class DomainLocationProfilesServiceV1ModelLocationData(object):
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
        'studios_for_rent': 'int',
        'terraced_houses_for_sale': 'int',
        'semi_detached_houses_for_sale': 'int',
        'townhouses_for_rent': 'int',
        'apartments_and_units_for_sale': 'int',
        'apartments_and_units_for_rent': 'int',
        'villas_for_sale': 'int',
        'duplexes_for_sale': 'int',
        'semi_detached_houses_for_rent': 'int',
        'studios_for_sale': 'int',
        'single_percentage': 'float',
        'most_common_age_bracket': 'str',
        'renter_percentage': 'float',
        'penthouses_for_sale': 'int',
        'villas_for_rent': 'int',
        'duplexes_for_rent': 'int',
        'houses_for_sale': 'int',
        'owner_occupier_percentage': 'float',
        'property_categories': 'list[DomainLocationProfilesServiceV1ModelLocationDataPropertyCategories]',
        'population': 'float',
        'penthouses_for_rent': 'int',
        'townhouses_for_sale': 'int',
        'terraced_houses_for_rent': 'int',
        'married_percentage': 'float',
        'houses_for_rent': 'int',
        'block_of_units_for_sale': 'int'
    }

    attribute_map = {
        'studios_for_rent': 'studiosForRent',
        'terraced_houses_for_sale': 'terracedHousesForSale',
        'semi_detached_houses_for_sale': 'semiDetachedHousesForSale',
        'townhouses_for_rent': 'townhousesForRent',
        'apartments_and_units_for_sale': 'apartmentsAndUnitsForSale',
        'apartments_and_units_for_rent': 'apartmentsAndUnitsForRent',
        'villas_for_sale': 'villasForSale',
        'duplexes_for_sale': 'duplexesForSale',
        'semi_detached_houses_for_rent': 'semiDetachedHousesForRent',
        'studios_for_sale': 'studiosForSale',
        'single_percentage': 'singlePercentage',
        'most_common_age_bracket': 'mostCommonAgeBracket',
        'renter_percentage': 'renterPercentage',
        'penthouses_for_sale': 'penthousesForSale',
        'villas_for_rent': 'villasForRent',
        'duplexes_for_rent': 'duplexesForRent',
        'houses_for_sale': 'housesForSale',
        'owner_occupier_percentage': 'ownerOccupierPercentage',
        'property_categories': 'propertyCategories',
        'population': 'population',
        'penthouses_for_rent': 'penthousesForRent',
        'townhouses_for_sale': 'townhousesForSale',
        'terraced_houses_for_rent': 'terracedHousesForRent',
        'married_percentage': 'marriedPercentage',
        'houses_for_rent': 'housesForRent',
        'block_of_units_for_sale': 'blockOfUnitsForSale'
    }

    def __init__(self, studios_for_rent=None, terraced_houses_for_sale=None, semi_detached_houses_for_sale=None, townhouses_for_rent=None, apartments_and_units_for_sale=None, apartments_and_units_for_rent=None, villas_for_sale=None, duplexes_for_sale=None, semi_detached_houses_for_rent=None, studios_for_sale=None, single_percentage=None, most_common_age_bracket=None, renter_percentage=None, penthouses_for_sale=None, villas_for_rent=None, duplexes_for_rent=None, houses_for_sale=None, owner_occupier_percentage=None, property_categories=None, population=None, penthouses_for_rent=None, townhouses_for_sale=None, terraced_houses_for_rent=None, married_percentage=None, houses_for_rent=None, block_of_units_for_sale=None):  # noqa: E501
        """DomainLocationProfilesServiceV1ModelLocationData - a model defined in Swagger"""  # noqa: E501

        self._studios_for_rent = None
        self._terraced_houses_for_sale = None
        self._semi_detached_houses_for_sale = None
        self._townhouses_for_rent = None
        self._apartments_and_units_for_sale = None
        self._apartments_and_units_for_rent = None
        self._villas_for_sale = None
        self._duplexes_for_sale = None
        self._semi_detached_houses_for_rent = None
        self._studios_for_sale = None
        self._single_percentage = None
        self._most_common_age_bracket = None
        self._renter_percentage = None
        self._penthouses_for_sale = None
        self._villas_for_rent = None
        self._duplexes_for_rent = None
        self._houses_for_sale = None
        self._owner_occupier_percentage = None
        self._property_categories = None
        self._population = None
        self._penthouses_for_rent = None
        self._townhouses_for_sale = None
        self._terraced_houses_for_rent = None
        self._married_percentage = None
        self._houses_for_rent = None
        self._block_of_units_for_sale = None
        self.discriminator = None

        if studios_for_rent is not None:
            self.studios_for_rent = studios_for_rent
        if terraced_houses_for_sale is not None:
            self.terraced_houses_for_sale = terraced_houses_for_sale
        if semi_detached_houses_for_sale is not None:
            self.semi_detached_houses_for_sale = semi_detached_houses_for_sale
        if townhouses_for_rent is not None:
            self.townhouses_for_rent = townhouses_for_rent
        if apartments_and_units_for_sale is not None:
            self.apartments_and_units_for_sale = apartments_and_units_for_sale
        if apartments_and_units_for_rent is not None:
            self.apartments_and_units_for_rent = apartments_and_units_for_rent
        if villas_for_sale is not None:
            self.villas_for_sale = villas_for_sale
        if duplexes_for_sale is not None:
            self.duplexes_for_sale = duplexes_for_sale
        if semi_detached_houses_for_rent is not None:
            self.semi_detached_houses_for_rent = semi_detached_houses_for_rent
        if studios_for_sale is not None:
            self.studios_for_sale = studios_for_sale
        if single_percentage is not None:
            self.single_percentage = single_percentage
        if most_common_age_bracket is not None:
            self.most_common_age_bracket = most_common_age_bracket
        if renter_percentage is not None:
            self.renter_percentage = renter_percentage
        if penthouses_for_sale is not None:
            self.penthouses_for_sale = penthouses_for_sale
        if villas_for_rent is not None:
            self.villas_for_rent = villas_for_rent
        if duplexes_for_rent is not None:
            self.duplexes_for_rent = duplexes_for_rent
        if houses_for_sale is not None:
            self.houses_for_sale = houses_for_sale
        if owner_occupier_percentage is not None:
            self.owner_occupier_percentage = owner_occupier_percentage
        if property_categories is not None:
            self.property_categories = property_categories
        if population is not None:
            self.population = population
        if penthouses_for_rent is not None:
            self.penthouses_for_rent = penthouses_for_rent
        if townhouses_for_sale is not None:
            self.townhouses_for_sale = townhouses_for_sale
        if terraced_houses_for_rent is not None:
            self.terraced_houses_for_rent = terraced_houses_for_rent
        if married_percentage is not None:
            self.married_percentage = married_percentage
        if houses_for_rent is not None:
            self.houses_for_rent = houses_for_rent
        if block_of_units_for_sale is not None:
            self.block_of_units_for_sale = block_of_units_for_sale

    @property
    def studios_for_rent(self):
        """Gets the studios_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The studios_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._studios_for_rent

    @studios_for_rent.setter
    def studios_for_rent(self, studios_for_rent):
        """Sets the studios_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.


        :param studios_for_rent: The studios_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._studios_for_rent = studios_for_rent

    @property
    def terraced_houses_for_sale(self):
        """Gets the terraced_houses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The terraced_houses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._terraced_houses_for_sale

    @terraced_houses_for_sale.setter
    def terraced_houses_for_sale(self, terraced_houses_for_sale):
        """Sets the terraced_houses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.


        :param terraced_houses_for_sale: The terraced_houses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._terraced_houses_for_sale = terraced_houses_for_sale

    @property
    def semi_detached_houses_for_sale(self):
        """Gets the semi_detached_houses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The semi_detached_houses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._semi_detached_houses_for_sale

    @semi_detached_houses_for_sale.setter
    def semi_detached_houses_for_sale(self, semi_detached_houses_for_sale):
        """Sets the semi_detached_houses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.


        :param semi_detached_houses_for_sale: The semi_detached_houses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._semi_detached_houses_for_sale = semi_detached_houses_for_sale

    @property
    def townhouses_for_rent(self):
        """Gets the townhouses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The townhouses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._townhouses_for_rent

    @townhouses_for_rent.setter
    def townhouses_for_rent(self, townhouses_for_rent):
        """Sets the townhouses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.


        :param townhouses_for_rent: The townhouses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._townhouses_for_rent = townhouses_for_rent

    @property
    def apartments_and_units_for_sale(self):
        """Gets the apartments_and_units_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The apartments_and_units_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._apartments_and_units_for_sale

    @apartments_and_units_for_sale.setter
    def apartments_and_units_for_sale(self, apartments_and_units_for_sale):
        """Sets the apartments_and_units_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.


        :param apartments_and_units_for_sale: The apartments_and_units_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._apartments_and_units_for_sale = apartments_and_units_for_sale

    @property
    def apartments_and_units_for_rent(self):
        """Gets the apartments_and_units_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The apartments_and_units_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._apartments_and_units_for_rent

    @apartments_and_units_for_rent.setter
    def apartments_and_units_for_rent(self, apartments_and_units_for_rent):
        """Sets the apartments_and_units_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.


        :param apartments_and_units_for_rent: The apartments_and_units_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._apartments_and_units_for_rent = apartments_and_units_for_rent

    @property
    def villas_for_sale(self):
        """Gets the villas_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The villas_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._villas_for_sale

    @villas_for_sale.setter
    def villas_for_sale(self, villas_for_sale):
        """Sets the villas_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.


        :param villas_for_sale: The villas_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._villas_for_sale = villas_for_sale

    @property
    def duplexes_for_sale(self):
        """Gets the duplexes_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The duplexes_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._duplexes_for_sale

    @duplexes_for_sale.setter
    def duplexes_for_sale(self, duplexes_for_sale):
        """Sets the duplexes_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.


        :param duplexes_for_sale: The duplexes_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._duplexes_for_sale = duplexes_for_sale

    @property
    def semi_detached_houses_for_rent(self):
        """Gets the semi_detached_houses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The semi_detached_houses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._semi_detached_houses_for_rent

    @semi_detached_houses_for_rent.setter
    def semi_detached_houses_for_rent(self, semi_detached_houses_for_rent):
        """Sets the semi_detached_houses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.


        :param semi_detached_houses_for_rent: The semi_detached_houses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._semi_detached_houses_for_rent = semi_detached_houses_for_rent

    @property
    def studios_for_sale(self):
        """Gets the studios_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The studios_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._studios_for_sale

    @studios_for_sale.setter
    def studios_for_sale(self, studios_for_sale):
        """Sets the studios_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.


        :param studios_for_sale: The studios_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._studios_for_sale = studios_for_sale

    @property
    def single_percentage(self):
        """Gets the single_percentage of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The single_percentage of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: float
        """
        return self._single_percentage

    @single_percentage.setter
    def single_percentage(self, single_percentage):
        """Sets the single_percentage of this DomainLocationProfilesServiceV1ModelLocationData.


        :param single_percentage: The single_percentage of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: float
        """

        self._single_percentage = single_percentage

    @property
    def most_common_age_bracket(self):
        """Gets the most_common_age_bracket of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The most_common_age_bracket of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: str
        """
        return self._most_common_age_bracket

    @most_common_age_bracket.setter
    def most_common_age_bracket(self, most_common_age_bracket):
        """Sets the most_common_age_bracket of this DomainLocationProfilesServiceV1ModelLocationData.


        :param most_common_age_bracket: The most_common_age_bracket of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: str
        """

        self._most_common_age_bracket = most_common_age_bracket

    @property
    def renter_percentage(self):
        """Gets the renter_percentage of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The renter_percentage of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: float
        """
        return self._renter_percentage

    @renter_percentage.setter
    def renter_percentage(self, renter_percentage):
        """Sets the renter_percentage of this DomainLocationProfilesServiceV1ModelLocationData.


        :param renter_percentage: The renter_percentage of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: float
        """

        self._renter_percentage = renter_percentage

    @property
    def penthouses_for_sale(self):
        """Gets the penthouses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The penthouses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._penthouses_for_sale

    @penthouses_for_sale.setter
    def penthouses_for_sale(self, penthouses_for_sale):
        """Sets the penthouses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.


        :param penthouses_for_sale: The penthouses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._penthouses_for_sale = penthouses_for_sale

    @property
    def villas_for_rent(self):
        """Gets the villas_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The villas_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._villas_for_rent

    @villas_for_rent.setter
    def villas_for_rent(self, villas_for_rent):
        """Sets the villas_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.


        :param villas_for_rent: The villas_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._villas_for_rent = villas_for_rent

    @property
    def duplexes_for_rent(self):
        """Gets the duplexes_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The duplexes_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._duplexes_for_rent

    @duplexes_for_rent.setter
    def duplexes_for_rent(self, duplexes_for_rent):
        """Sets the duplexes_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.


        :param duplexes_for_rent: The duplexes_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._duplexes_for_rent = duplexes_for_rent

    @property
    def houses_for_sale(self):
        """Gets the houses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The houses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._houses_for_sale

    @houses_for_sale.setter
    def houses_for_sale(self, houses_for_sale):
        """Sets the houses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.


        :param houses_for_sale: The houses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._houses_for_sale = houses_for_sale

    @property
    def owner_occupier_percentage(self):
        """Gets the owner_occupier_percentage of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The owner_occupier_percentage of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: float
        """
        return self._owner_occupier_percentage

    @owner_occupier_percentage.setter
    def owner_occupier_percentage(self, owner_occupier_percentage):
        """Sets the owner_occupier_percentage of this DomainLocationProfilesServiceV1ModelLocationData.


        :param owner_occupier_percentage: The owner_occupier_percentage of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: float
        """

        self._owner_occupier_percentage = owner_occupier_percentage

    @property
    def property_categories(self):
        """Gets the property_categories of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The property_categories of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: list[DomainLocationProfilesServiceV1ModelLocationDataPropertyCategories]
        """
        return self._property_categories

    @property_categories.setter
    def property_categories(self, property_categories):
        """Sets the property_categories of this DomainLocationProfilesServiceV1ModelLocationData.


        :param property_categories: The property_categories of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: list[DomainLocationProfilesServiceV1ModelLocationDataPropertyCategories]
        """

        self._property_categories = property_categories

    @property
    def population(self):
        """Gets the population of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The population of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: float
        """
        return self._population

    @population.setter
    def population(self, population):
        """Sets the population of this DomainLocationProfilesServiceV1ModelLocationData.


        :param population: The population of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: float
        """

        self._population = population

    @property
    def penthouses_for_rent(self):
        """Gets the penthouses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The penthouses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._penthouses_for_rent

    @penthouses_for_rent.setter
    def penthouses_for_rent(self, penthouses_for_rent):
        """Sets the penthouses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.


        :param penthouses_for_rent: The penthouses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._penthouses_for_rent = penthouses_for_rent

    @property
    def townhouses_for_sale(self):
        """Gets the townhouses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The townhouses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._townhouses_for_sale

    @townhouses_for_sale.setter
    def townhouses_for_sale(self, townhouses_for_sale):
        """Sets the townhouses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.


        :param townhouses_for_sale: The townhouses_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._townhouses_for_sale = townhouses_for_sale

    @property
    def terraced_houses_for_rent(self):
        """Gets the terraced_houses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The terraced_houses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._terraced_houses_for_rent

    @terraced_houses_for_rent.setter
    def terraced_houses_for_rent(self, terraced_houses_for_rent):
        """Sets the terraced_houses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.


        :param terraced_houses_for_rent: The terraced_houses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._terraced_houses_for_rent = terraced_houses_for_rent

    @property
    def married_percentage(self):
        """Gets the married_percentage of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The married_percentage of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: float
        """
        return self._married_percentage

    @married_percentage.setter
    def married_percentage(self, married_percentage):
        """Sets the married_percentage of this DomainLocationProfilesServiceV1ModelLocationData.


        :param married_percentage: The married_percentage of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: float
        """

        self._married_percentage = married_percentage

    @property
    def houses_for_rent(self):
        """Gets the houses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The houses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._houses_for_rent

    @houses_for_rent.setter
    def houses_for_rent(self, houses_for_rent):
        """Sets the houses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.


        :param houses_for_rent: The houses_for_rent of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._houses_for_rent = houses_for_rent

    @property
    def block_of_units_for_sale(self):
        """Gets the block_of_units_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501


        :return: The block_of_units_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :rtype: int
        """
        return self._block_of_units_for_sale

    @block_of_units_for_sale.setter
    def block_of_units_for_sale(self, block_of_units_for_sale):
        """Sets the block_of_units_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.


        :param block_of_units_for_sale: The block_of_units_for_sale of this DomainLocationProfilesServiceV1ModelLocationData.  # noqa: E501
        :type: int
        """

        self._block_of_units_for_sale = block_of_units_for_sale

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
        if issubclass(DomainLocationProfilesServiceV1ModelLocationData, dict):
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
        if not isinstance(other, DomainLocationProfilesServiceV1ModelLocationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
