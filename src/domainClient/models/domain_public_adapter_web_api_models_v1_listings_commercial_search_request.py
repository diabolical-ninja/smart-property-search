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


class DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest(object):
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
        'page_number': 'int',
        'advertiser_id': 'int',
        'page_size': 'int',
        'property_types': 'list[str]',
        'price': 'DomainPublicAdapterWebApiModelsV1ListingsCommercialPriceSearch',
        'locations': 'list[DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch]',
        'keywords': 'list[str]',
        'geo_window': 'DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoWindow',
        'land_area_min': 'int',
        'land_area_max': 'int',
        'building_size_min': 'int',
        'building_size_max': 'int',
        'search_mode': 'str',
        'occupancy': 'str',
        'sort': 'str',
        'sale_type': 'str',
        'property_title': 'str',
        'parking': 'DomainPublicAdapterWebApiModelsV1ListingsCommercialParkingSearch',
        'exclusion_types': 'list[str]',
        'annual_return': 'int'
    }

    attribute_map = {
        'page_number': 'pageNumber',
        'advertiser_id': 'advertiserId',
        'page_size': 'pageSize',
        'property_types': 'propertyTypes',
        'price': 'price',
        'locations': 'locations',
        'keywords': 'keywords',
        'geo_window': 'geoWindow',
        'land_area_min': 'landAreaMin',
        'land_area_max': 'landAreaMax',
        'building_size_min': 'buildingSizeMin',
        'building_size_max': 'buildingSizeMax',
        'search_mode': 'searchMode',
        'occupancy': 'occupancy',
        'sort': 'sort',
        'sale_type': 'saleType',
        'property_title': 'propertyTitle',
        'parking': 'parking',
        'exclusion_types': 'exclusionTypes',
        'annual_return': 'annualReturn'
    }

    def __init__(self, page_number=None, advertiser_id=None, page_size=None, property_types=None, price=None, locations=None, keywords=None, geo_window=None, land_area_min=None, land_area_max=None, building_size_min=None, building_size_max=None, search_mode=None, occupancy=None, sort=None, sale_type=None, property_title=None, parking=None, exclusion_types=None, annual_return=None):  # noqa: E501
        """DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest - a model defined in Swagger"""  # noqa: E501

        self._page_number = None
        self._advertiser_id = None
        self._page_size = None
        self._property_types = None
        self._price = None
        self._locations = None
        self._keywords = None
        self._geo_window = None
        self._land_area_min = None
        self._land_area_max = None
        self._building_size_min = None
        self._building_size_max = None
        self._search_mode = None
        self._occupancy = None
        self._sort = None
        self._sale_type = None
        self._property_title = None
        self._parking = None
        self._exclusion_types = None
        self._annual_return = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        if advertiser_id is not None:
            self.advertiser_id = advertiser_id
        if page_size is not None:
            self.page_size = page_size
        if property_types is not None:
            self.property_types = property_types
        if price is not None:
            self.price = price
        if locations is not None:
            self.locations = locations
        if keywords is not None:
            self.keywords = keywords
        if geo_window is not None:
            self.geo_window = geo_window
        if land_area_min is not None:
            self.land_area_min = land_area_min
        if land_area_max is not None:
            self.land_area_max = land_area_max
        if building_size_min is not None:
            self.building_size_min = building_size_min
        if building_size_max is not None:
            self.building_size_max = building_size_max
        if search_mode is not None:
            self.search_mode = search_mode
        if occupancy is not None:
            self.occupancy = occupancy
        if sort is not None:
            self.sort = sort
        if sale_type is not None:
            self.sale_type = sale_type
        if property_title is not None:
            self.property_title = property_title
        if parking is not None:
            self.parking = parking
        if exclusion_types is not None:
            self.exclusion_types = exclusion_types
        if annual_return is not None:
            self.annual_return = annual_return

    @property
    def page_number(self):
        """Gets the page_number of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

          # noqa: E501

        :return: The page_number of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

          # noqa: E501

        :param page_number: The page_number of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def advertiser_id(self):
        """Gets the advertiser_id of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Agency ID  # noqa: E501

        :return: The advertiser_id of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._advertiser_id

    @advertiser_id.setter
    def advertiser_id(self, advertiser_id):
        """Sets the advertiser_id of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Agency ID  # noqa: E501

        :param advertiser_id: The advertiser_id of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: int
        """

        self._advertiser_id = advertiser_id

    @property
    def page_size(self):
        """Gets the page_size of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Search results page size  # noqa: E501

        :return: The page_size of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Search results page size  # noqa: E501

        :param page_size: The page_size of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def property_types(self):
        """Gets the property_types of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Listing property types  # noqa: E501

        :return: The property_types of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._property_types

    @property_types.setter
    def property_types(self, property_types):
        """Sets the property_types of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Listing property types  # noqa: E501

        :param property_types: The property_types of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["unknown", "accessoriesParts", "accommodationTourism", "accounting", "acreageSemiRural", "adult", "advertisingMarketing", "aerial", "aeronautical", "agedCare", "agricultural", "air", "aircraft", "alarms", "alcoholLiquor", "amusements", "animalRelated", "apartmentUnitFlat", "aquaculture", "aquaticMarineMarinaBerth", "artsCrafts", "autoElectrical", "automotive", "backpackerHostel", "bakery", "barsNightclubs", "beautyHealth", "beautyProducts", "beautySalon", "bedAndBreakfast", "bikeAndMotorcycle", "blockOfUnits", "boardingKennels", "boatsMarineMarinaBerth", "bookkeeping", "brokerage", "builder", "buildingAndConstruction", "bus", "butcher", "cafeCoffeeShop", "car", "carBusTruck", "carDealership", "carRental", "carSpace", "carWash", "caravanPark", "carpenter", "catering", "childCare", "civil", "cleaning", "cleaningAndMaintenance", "clinicalPractice", "clothingAccessories", "clothingFootwear", "communication", "communications", "computerIT", "computerAndInternet", "construction", "convenienceStore", "copyLaminate", "courier", "cropHarvesting", "customs", "dairyFarming", "deli", "dental", "detailing", "developmentLand", "developmentSite", "distributors", "drivingSchools", "duplex", "educationTraining", "educational", "electrical", "employmentRecruitment", "entertainment", "entertainmentTechnology", "export", "farm", "farming", "fertiliser", "finance", "financialServices", "fishingForestry", "floristNursery", "foodBeverage", "foodBeverageHospitality", "franchiseBusinessOpportunities", "freight", "fruitVegFreshProduce", "fruitPicking", "functionCentre", "furnitureTimber", "gambling", "gardenHousehold", "gardenNurseries", "gardening", "glassCeramic", "guestHouseBB", "guesthouse", "hairdresser", "healthBeauty", "healthSpa", "hire", "homeGarden", "homeBased", "newHomeDesigns", "homewareHardware", "hospital", "hotel", "hotelLeisure", "hotelMotelPub", "house", "newHouseLand", "huntingTrap", "import", "importExportWholesale", "industrialManufacturing", "industrialWarehouse", "insemination", "insurance", "internationalNewDevelopment", "internet", "irrigationServices", "juiceBar", "landClearing", "newLand", "landscaping", "laundryDryCleaning", "legal", "leisureEntertainment", "limousineTaxi", "livestock", "internationalCommercial", "machinery", "machineryMetal", "managementRights", "manufacturers", "manufacturingEngineering", "marine", "massage", "mechanicalRepair", "media", "medical", "medicalConsulting", "medicalPractice", "miningEarthMoving", "mobileServices", "motel", "motorcycle", "musicRelated", "mustering", "nails", "naturalTherapies", "newApartments", "newsagency", "nursery", "nursingHome", "offices", "officeSupplies", "oilGas", "onStreet", "panelBeating", "paperPrinting", "parkingCarSpace", "penthouse", "pestRelated", "pharmacies", "plastic", "plumbing", "poolWater", "postOffices", "printPhoto", "professional", "propertyRealEstate", "rail", "recreationSport", "recruitment", "repair", "resort", "restaurant", "retail", "retailer", "retirementVillage", "road", "rural", "ruralCommercialFarming", "scientific", "sea", "security", "semiDetached", "serviceStation", "serviced", "services", "shearing", "showroomsBulkyGoods", "specialistFarm", "sportsComplexGym", "studio", "supermarket", "takeawayFood", "taxi", "terrace", "themePark", "tours", "townhouse", "training", "transportDistribution", "travel", "truck", "vacantLand", "vending", "villa", "water", "welding", "wholesale", "wholesalers", "withShowroomWarehouse", "withinShoppingComplex", "woolClassing", "wreckers", "tattersalls", "servicedOffices", "other", "alcoholGrocery", "cafeRestaurant", "discountStore", "ecoFriendly", "green", "grocery", "specialityRetail", "storage", "travelAgency", "varietyStore", "franchiseNew", "business"]  # noqa: E501
        if not set(property_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `property_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(property_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._property_types = property_types

    @property
    def price(self):
        """Gets the price of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Price search criteria  # noqa: E501

        :return: The price of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: DomainPublicAdapterWebApiModelsV1ListingsCommercialPriceSearch
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Price search criteria  # noqa: E501

        :param price: The price of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: DomainPublicAdapterWebApiModelsV1ListingsCommercialPriceSearch
        """

        self._price = price

    @property
    def locations(self):
        """Gets the locations of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Location search criteria  # noqa: E501

        :return: The locations of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: list[DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Location search criteria  # noqa: E501

        :param locations: The locations of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: list[DomainPublicAdapterWebApiModelsV1ListingsCommercialLocationSearch]
        """

        self._locations = locations

    @property
    def keywords(self):
        """Gets the keywords of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Search listings by keyword  # noqa: E501

        :return: The keywords of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Search listings by keyword  # noqa: E501

        :param keywords: The keywords of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def geo_window(self):
        """Gets the geo_window of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Geospatial search (polygon)  # noqa: E501

        :return: The geo_window of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoWindow
        """
        return self._geo_window

    @geo_window.setter
    def geo_window(self, geo_window):
        """Sets the geo_window of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Geospatial search (polygon)  # noqa: E501

        :param geo_window: The geo_window of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoWindow
        """

        self._geo_window = geo_window

    @property
    def land_area_min(self):
        """Gets the land_area_min of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Minimum land area  # noqa: E501

        :return: The land_area_min of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._land_area_min

    @land_area_min.setter
    def land_area_min(self, land_area_min):
        """Sets the land_area_min of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Minimum land area  # noqa: E501

        :param land_area_min: The land_area_min of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: int
        """

        self._land_area_min = land_area_min

    @property
    def land_area_max(self):
        """Gets the land_area_max of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Maximum land area  # noqa: E501

        :return: The land_area_max of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._land_area_max

    @land_area_max.setter
    def land_area_max(self, land_area_max):
        """Sets the land_area_max of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Maximum land area  # noqa: E501

        :param land_area_max: The land_area_max of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: int
        """

        self._land_area_max = land_area_max

    @property
    def building_size_min(self):
        """Gets the building_size_min of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Minimum building area  # noqa: E501

        :return: The building_size_min of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._building_size_min

    @building_size_min.setter
    def building_size_min(self, building_size_min):
        """Sets the building_size_min of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Minimum building area  # noqa: E501

        :param building_size_min: The building_size_min of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: int
        """

        self._building_size_min = building_size_min

    @property
    def building_size_max(self):
        """Gets the building_size_max of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Maximum building area  # noqa: E501

        :return: The building_size_max of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._building_size_max

    @building_size_max.setter
    def building_size_max(self, building_size_max):
        """Sets the building_size_max of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Maximum building area  # noqa: E501

        :param building_size_max: The building_size_max of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: int
        """

        self._building_size_max = building_size_max

    @property
    def search_mode(self):
        """Gets the search_mode of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Search mode  # noqa: E501

        :return: The search_mode of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._search_mode

    @search_mode.setter
    def search_mode(self, search_mode):
        """Sets the search_mode of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Search mode  # noqa: E501

        :param search_mode: The search_mode of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["forSale", "forLease", "sold", "leased"]  # noqa: E501
        if search_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `search_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(search_mode, allowed_values)
            )

        self._search_mode = search_mode

    @property
    def occupancy(self):
        """Gets the occupancy of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Occupancy  # noqa: E501

        :return: The occupancy of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._occupancy

    @occupancy.setter
    def occupancy(self, occupancy):
        """Sets the occupancy of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Occupancy  # noqa: E501

        :param occupancy: The occupancy of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: str
        """

        self._occupancy = occupancy

    @property
    def sort(self):
        """Gets the sort of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Sorting order  # noqa: E501

        :return: The sort of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Sorting order  # noqa: E501

        :param sort: The sort of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["default", "newestFirst", "cheapestTotalFirst", "cheapestPerSqmFirst", "mostExpensiveTotalFirst", "mostExpensivePerSqmFirst", "suburbAsc", "suburbDesc", "buildingSizeAsc", "buildingSizeDesc"]  # noqa: E501
        if sort not in allowed_values:
            raise ValueError(
                "Invalid value for `sort` ({0}), must be one of {1}"  # noqa: E501
                .format(sort, allowed_values)
            )

        self._sort = sort

    @property
    def sale_type(self):
        """Gets the sale_type of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Sale type  # noqa: E501

        :return: The sale_type of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._sale_type

    @sale_type.setter
    def sale_type(self, sale_type):
        """Sets the sale_type of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Sale type  # noqa: E501

        :param sale_type: The sale_type of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["standardSale", "auction", "expressionOfInterest", "tender"]  # noqa: E501
        if sale_type not in allowed_values:
            raise ValueError(
                "Invalid value for `sale_type` ({0}), must be one of {1}"  # noqa: E501
                .format(sale_type, allowed_values)
            )

        self._sale_type = sale_type

    @property
    def property_title(self):
        """Gets the property_title of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Property title  # noqa: E501

        :return: The property_title of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._property_title

    @property_title.setter
    def property_title(self, property_title):
        """Sets the property_title of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Property title  # noqa: E501

        :param property_title: The property_title of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["freehold", "strata", "noBuilding"]  # noqa: E501
        if property_title not in allowed_values:
            raise ValueError(
                "Invalid value for `property_title` ({0}), must be one of {1}"  # noqa: E501
                .format(property_title, allowed_values)
            )

        self._property_title = property_title

    @property
    def parking(self):
        """Gets the parking of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Parking search criteria  # noqa: E501

        :return: The parking of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: DomainPublicAdapterWebApiModelsV1ListingsCommercialParkingSearch
        """
        return self._parking

    @parking.setter
    def parking(self, parking):
        """Sets the parking of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Parking search criteria  # noqa: E501

        :param parking: The parking of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: DomainPublicAdapterWebApiModelsV1ListingsCommercialParkingSearch
        """

        self._parking = parking

    @property
    def exclusion_types(self):
        """Gets the exclusion_types of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Exclusion Types  # noqa: E501

        :return: The exclusion_types of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclusion_types

    @exclusion_types.setter
    def exclusion_types(self, exclusion_types):
        """Sets the exclusion_types of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Exclusion Types  # noqa: E501

        :param exclusion_types: The exclusion_types of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["surroundingSuburbs", "withoutPrice"]  # noqa: E501
        if not set(exclusion_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `exclusion_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(exclusion_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._exclusion_types = exclusion_types

    @property
    def annual_return(self):
        """Gets the annual_return of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501

        Minimum annual return (in percents)  # noqa: E501

        :return: The annual_return of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._annual_return

    @annual_return.setter
    def annual_return(self, annual_return):
        """Sets the annual_return of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.

        Minimum annual return (in percents)  # noqa: E501

        :param annual_return: The annual_return of this DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest.  # noqa: E501
        :type: int
        """

        self._annual_return = annual_return

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
        if issubclass(DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest, dict):
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
        if not isinstance(other, DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
