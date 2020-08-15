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


class DomainListingAdminServiceV1ModelBusinessProperty(object):
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
        'property_type': 'list[str]',
        'land_area': 'DomainListingAdminServiceV1ModelLandArea',
        'images': 'list[DomainListingAdminServiceV1ModelPropertyMedia]',
        'address': 'DomainListingAdminServiceV1ModelAddress',
        'parking': 'DomainListingAdminServiceV1ModelParking',
        'area': 'DomainListingAdminServiceV1ModelArea',
        'pdfs': 'list[DomainListingAdminServiceV1ModelPropertyPdf]',
        'is_marked_for_liveability': 'bool',
        'property_name': 'str',
        'location': 'str'
    }

    attribute_map = {
        'property_type': 'propertyType',
        'land_area': 'landArea',
        'images': 'images',
        'address': 'address',
        'parking': 'parking',
        'area': 'area',
        'pdfs': 'pdfs',
        'is_marked_for_liveability': 'isMarkedForLiveability',
        'property_name': 'propertyName',
        'location': 'location'
    }

    def __init__(self, property_type=None, land_area=None, images=None, address=None, parking=None, area=None, pdfs=None, is_marked_for_liveability=None, property_name=None, location=None):  # noqa: E501
        """DomainListingAdminServiceV1ModelBusinessProperty - a model defined in Swagger"""  # noqa: E501

        self._property_type = None
        self._land_area = None
        self._images = None
        self._address = None
        self._parking = None
        self._area = None
        self._pdfs = None
        self._is_marked_for_liveability = None
        self._property_name = None
        self._location = None
        self.discriminator = None

        if property_type is not None:
            self.property_type = property_type
        if land_area is not None:
            self.land_area = land_area
        if images is not None:
            self.images = images
        if address is not None:
            self.address = address
        if parking is not None:
            self.parking = parking
        if area is not None:
            self.area = area
        if pdfs is not None:
            self.pdfs = pdfs
        if is_marked_for_liveability is not None:
            self.is_marked_for_liveability = is_marked_for_liveability
        if property_name is not None:
            self.property_name = property_name
        if location is not None:
            self.location = location

    @property
    def property_type(self):
        """Gets the property_type of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501

        Business property types ['accessoriesParts', 'accommodationTourism', 'accounting', 'adult', 'advertisingMarketing', 'aerial', 'aeronautical', 'agedCare', 'agricultural', 'air', 'aircraft', 'alarms', 'alcoholLiquor', 'amusements', 'animalRelated', 'aquaculture', 'aquaticMarineMarinaBerth', 'artsCrafts', 'autoElectrical', 'automotive', 'backpackerHostel', 'bakery', 'barsNightclubs', 'beautyHealth', 'beautyProducts', 'beautySalon', 'bikeAndMotorcycle', 'boardingKennels', 'boatsMarineMarinaBerth', 'bookkeeping', 'brokerage', 'builder', 'buildingAndConstruction', 'bus', 'butcher', 'cafeCoffeeShop', 'car', 'carBusTruck', 'carDealership', 'carRental', 'carWash', 'caravanPark', 'carpenter', 'catering', 'childCare', 'civil', 'cleaning', 'cleaningAndMaintenance', 'clinicalPractice', 'clothingAccessories', 'clothingFootwear', 'communication', 'communications', 'computerIT', 'computerAndInternet', 'construction', 'convenienceStore', 'copyLaminate', 'courier', 'cropHarvesting', 'customs', 'dairyFarming', 'deli', 'dental', 'detailing', 'distributors', 'drivingSchools', 'educationTraining', 'educational', 'electrical', 'employmentRecruitment', 'entertainment', 'entertainmentTechnology', 'export', 'farming', 'fertiliser', 'finance', 'financialServices', 'fishingForestry', 'floristNursery', 'foodBeverage', 'foodBeverageHospitality', 'franchiseBusinessOpportunities', 'freight', 'fruitVegFreshProduce', 'fruitPicking', 'functionCentre', 'furnitureTimber', 'gambling', 'gardenHousehold', 'gardenNurseries', 'gardening', 'glassCeramic', 'guestHouseBB', 'hairdresser', 'healthBeauty', 'healthSpa', 'hire', 'homeGarden', 'homeBased', 'homewareHardware', 'hospital', 'hotel', 'huntingTrap', 'import', 'importExportWholesale', 'industrialManufacturing', 'insemination', 'insurance', 'internet', 'irrigationServices', 'juiceBar', 'landClearing', 'landscaping', 'laundryDryCleaning', 'legal', 'leisureEntertainment', 'limousineTaxi', 'livestock', 'machinery', 'machineryMetal', 'managementRights', 'manufacturers', 'manufacturingEngineering', 'marine', 'massage', 'mechanicalRepair', 'media', 'medical', 'medicalPractice', 'miningEarthMoving', 'mobileServices', 'motel', 'motorcycle', 'musicRelated', 'mustering', 'nails', 'naturalTherapies', 'newsagency', 'nursery', 'nursingHome', 'officeSupplies', 'oilGas', 'panelBeating', 'paperPrinting', 'parkingCarSpace', 'pestRelated', 'pharmacies', 'plastic', 'plumbing', 'poolWater', 'postOffices', 'printPhoto', 'professional', 'propertyRealEstate', 'rail', 'recreationSport', 'recruitment', 'repair', 'resort', 'restaurant', 'retail', 'retailer', 'retirement', 'retirementVillage', 'road', 'rural', 'scientific', 'sea', 'security', 'serviceStation', 'services', 'shearing', 'sportsComplexGym', 'supermarket', 'takeawayFood', 'taxi', 'themePark', 'tours', 'training', 'transportDistribution', 'travel', 'truck', 'vending', 'water', 'welding', 'wholesale', 'wholesalers', 'woolClassing', 'wreckers', 'alcoholGrocery', 'cafeRestaurants', 'discountStore', 'ecoFriendly', 'green', 'grocery', 'specialityRetail', 'storage', 'travelAgency', 'varietyStore', 'chickenShop', 'seafoodShop', 'deliCafe', 'cropping', 'viticulture', 'grazing', 'horticulture', 'equine', 'farmlet', 'orchard', 'ruralLifestyle', 'onlineBusiness'].  # noqa: E501

        :return: The property_type of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :rtype: list[str]
        """
        return self._property_type

    @property_type.setter
    def property_type(self, property_type):
        """Sets the property_type of this DomainListingAdminServiceV1ModelBusinessProperty.

        Business property types ['accessoriesParts', 'accommodationTourism', 'accounting', 'adult', 'advertisingMarketing', 'aerial', 'aeronautical', 'agedCare', 'agricultural', 'air', 'aircraft', 'alarms', 'alcoholLiquor', 'amusements', 'animalRelated', 'aquaculture', 'aquaticMarineMarinaBerth', 'artsCrafts', 'autoElectrical', 'automotive', 'backpackerHostel', 'bakery', 'barsNightclubs', 'beautyHealth', 'beautyProducts', 'beautySalon', 'bikeAndMotorcycle', 'boardingKennels', 'boatsMarineMarinaBerth', 'bookkeeping', 'brokerage', 'builder', 'buildingAndConstruction', 'bus', 'butcher', 'cafeCoffeeShop', 'car', 'carBusTruck', 'carDealership', 'carRental', 'carWash', 'caravanPark', 'carpenter', 'catering', 'childCare', 'civil', 'cleaning', 'cleaningAndMaintenance', 'clinicalPractice', 'clothingAccessories', 'clothingFootwear', 'communication', 'communications', 'computerIT', 'computerAndInternet', 'construction', 'convenienceStore', 'copyLaminate', 'courier', 'cropHarvesting', 'customs', 'dairyFarming', 'deli', 'dental', 'detailing', 'distributors', 'drivingSchools', 'educationTraining', 'educational', 'electrical', 'employmentRecruitment', 'entertainment', 'entertainmentTechnology', 'export', 'farming', 'fertiliser', 'finance', 'financialServices', 'fishingForestry', 'floristNursery', 'foodBeverage', 'foodBeverageHospitality', 'franchiseBusinessOpportunities', 'freight', 'fruitVegFreshProduce', 'fruitPicking', 'functionCentre', 'furnitureTimber', 'gambling', 'gardenHousehold', 'gardenNurseries', 'gardening', 'glassCeramic', 'guestHouseBB', 'hairdresser', 'healthBeauty', 'healthSpa', 'hire', 'homeGarden', 'homeBased', 'homewareHardware', 'hospital', 'hotel', 'huntingTrap', 'import', 'importExportWholesale', 'industrialManufacturing', 'insemination', 'insurance', 'internet', 'irrigationServices', 'juiceBar', 'landClearing', 'landscaping', 'laundryDryCleaning', 'legal', 'leisureEntertainment', 'limousineTaxi', 'livestock', 'machinery', 'machineryMetal', 'managementRights', 'manufacturers', 'manufacturingEngineering', 'marine', 'massage', 'mechanicalRepair', 'media', 'medical', 'medicalPractice', 'miningEarthMoving', 'mobileServices', 'motel', 'motorcycle', 'musicRelated', 'mustering', 'nails', 'naturalTherapies', 'newsagency', 'nursery', 'nursingHome', 'officeSupplies', 'oilGas', 'panelBeating', 'paperPrinting', 'parkingCarSpace', 'pestRelated', 'pharmacies', 'plastic', 'plumbing', 'poolWater', 'postOffices', 'printPhoto', 'professional', 'propertyRealEstate', 'rail', 'recreationSport', 'recruitment', 'repair', 'resort', 'restaurant', 'retail', 'retailer', 'retirement', 'retirementVillage', 'road', 'rural', 'scientific', 'sea', 'security', 'serviceStation', 'services', 'shearing', 'sportsComplexGym', 'supermarket', 'takeawayFood', 'taxi', 'themePark', 'tours', 'training', 'transportDistribution', 'travel', 'truck', 'vending', 'water', 'welding', 'wholesale', 'wholesalers', 'woolClassing', 'wreckers', 'alcoholGrocery', 'cafeRestaurants', 'discountStore', 'ecoFriendly', 'green', 'grocery', 'specialityRetail', 'storage', 'travelAgency', 'varietyStore', 'chickenShop', 'seafoodShop', 'deliCafe', 'cropping', 'viticulture', 'grazing', 'horticulture', 'equine', 'farmlet', 'orchard', 'ruralLifestyle', 'onlineBusiness'].  # noqa: E501

        :param property_type: The property_type of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["accessoriesParts", "accommodationTourism", "accounting", "adult", "advertisingMarketing", "aerial", "aeronautical", "agedCare", "agricultural", "air", "aircraft", "alarms", "alcoholLiquor", "amusements", "animalRelated", "aquaculture", "aquaticMarineMarinaBerth", "artsCrafts", "autoElectrical", "automotive", "backpackerHostel", "bakery", "barsNightclubs", "beautyHealth", "beautyProducts", "beautySalon", "bikeAndMotorcycle", "boardingKennels", "boatsMarineMarinaBerth", "bookkeeping", "brokerage", "builder", "buildingAndConstruction", "bus", "butcher", "cafeCoffeeShop", "car", "carBusTruck", "carDealership", "carRental", "carWash", "caravanPark", "carpenter", "catering", "childCare", "civil", "cleaning", "cleaningAndMaintenance", "clinicalPractice", "clothingAccessories", "clothingFootwear", "communication", "communications", "computerIT", "computerAndInternet", "construction", "convenienceStore", "copyLaminate", "courier", "cropHarvesting", "customs", "dairyFarming", "deli", "dental", "detailing", "distributors", "drivingSchools", "educationTraining", "educational", "electrical", "employmentRecruitment", "entertainment", "entertainmentTechnology", "export", "farming", "fertiliser", "finance", "financialServices", "fishingForestry", "floristNursery", "foodBeverage", "foodBeverageHospitality", "franchiseBusinessOpportunities", "freight", "fruitVegFreshProduce", "fruitPicking", "functionCentre", "furnitureTimber", "gambling", "gardenHousehold", "gardenNurseries", "gardening", "glassCeramic", "guestHouseBB", "hairdresser", "healthBeauty", "healthSpa", "hire", "homeGarden", "homeBased", "homewareHardware", "hospital", "hotel", "huntingTrap", "import", "importExportWholesale", "industrialManufacturing", "insemination", "insurance", "internet", "irrigationServices", "juiceBar", "landClearing", "landscaping", "laundryDryCleaning", "legal", "leisureEntertainment", "limousineTaxi", "livestock", "machinery", "machineryMetal", "managementRights", "manufacturers", "manufacturingEngineering", "marine", "massage", "mechanicalRepair", "media", "medical", "medicalPractice", "miningEarthMoving", "mobileServices", "motel", "motorcycle", "musicRelated", "mustering", "nails", "naturalTherapies", "newsagency", "nursery", "nursingHome", "officeSupplies", "oilGas", "panelBeating", "paperPrinting", "parkingCarSpace", "pestRelated", "pharmacies", "plastic", "plumbing", "poolWater", "postOffices", "printPhoto", "professional", "propertyRealEstate", "rail", "recreationSport", "recruitment", "repair", "resort", "restaurant", "retail", "retailer", "retirement", "retirementVillage", "road", "rural", "scientific", "sea", "security", "serviceStation", "services", "shearing", "sportsComplexGym", "supermarket", "takeawayFood", "taxi", "themePark", "tours", "training", "transportDistribution", "travel", "truck", "vending", "water", "welding", "wholesale", "wholesalers", "woolClassing", "wreckers", "alcoholGrocery", "cafeRestaurants", "discountStore", "ecoFriendly", "green", "grocery", "specialityRetail", "storage", "travelAgency", "varietyStore", "chickenShop", "seafoodShop", "deliCafe", "cropping", "viticulture", "grazing", "horticulture", "equine", "farmlet", "orchard", "ruralLifestyle", "onlineBusiness"]  # noqa: E501
        if not set(property_type).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `property_type` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(property_type) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._property_type = property_type

    @property
    def land_area(self):
        """Gets the land_area of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501

        Land Area  # noqa: E501

        :return: The land_area of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :rtype: DomainListingAdminServiceV1ModelLandArea
        """
        return self._land_area

    @land_area.setter
    def land_area(self, land_area):
        """Sets the land_area of this DomainListingAdminServiceV1ModelBusinessProperty.

        Land Area  # noqa: E501

        :param land_area: The land_area of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :type: DomainListingAdminServiceV1ModelLandArea
        """

        self._land_area = land_area

    @property
    def images(self):
        """Gets the images of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501

        List of image files, photos or floor plans related to the listing  # noqa: E501

        :return: The images of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :rtype: list[DomainListingAdminServiceV1ModelPropertyMedia]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this DomainListingAdminServiceV1ModelBusinessProperty.

        List of image files, photos or floor plans related to the listing  # noqa: E501

        :param images: The images of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :type: list[DomainListingAdminServiceV1ModelPropertyMedia]
        """

        self._images = images

    @property
    def address(self):
        """Gets the address of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501

        Address Details  # noqa: E501

        :return: The address of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :rtype: DomainListingAdminServiceV1ModelAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this DomainListingAdminServiceV1ModelBusinessProperty.

        Address Details  # noqa: E501

        :param address: The address of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :type: DomainListingAdminServiceV1ModelAddress
        """

        self._address = address

    @property
    def parking(self):
        """Gets the parking of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501

        Parking Details  # noqa: E501

        :return: The parking of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :rtype: DomainListingAdminServiceV1ModelParking
        """
        return self._parking

    @parking.setter
    def parking(self, parking):
        """Sets the parking of this DomainListingAdminServiceV1ModelBusinessProperty.

        Parking Details  # noqa: E501

        :param parking: The parking of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :type: DomainListingAdminServiceV1ModelParking
        """

        self._parking = parking

    @property
    def area(self):
        """Gets the area of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501

        Building area in square metres  # noqa: E501

        :return: The area of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :rtype: DomainListingAdminServiceV1ModelArea
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this DomainListingAdminServiceV1ModelBusinessProperty.

        Building area in square metres  # noqa: E501

        :param area: The area of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :type: DomainListingAdminServiceV1ModelArea
        """

        self._area = area

    @property
    def pdfs(self):
        """Gets the pdfs of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501

        List of PDF files related to the listing  # noqa: E501

        :return: The pdfs of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :rtype: list[DomainListingAdminServiceV1ModelPropertyPdf]
        """
        return self._pdfs

    @pdfs.setter
    def pdfs(self, pdfs):
        """Sets the pdfs of this DomainListingAdminServiceV1ModelBusinessProperty.

        List of PDF files related to the listing  # noqa: E501

        :param pdfs: The pdfs of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :type: list[DomainListingAdminServiceV1ModelPropertyPdf]
        """

        self._pdfs = pdfs

    @property
    def is_marked_for_liveability(self):
        """Gets the is_marked_for_liveability of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501

        Is the property liveability compliant  # noqa: E501

        :return: The is_marked_for_liveability of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :rtype: bool
        """
        return self._is_marked_for_liveability

    @is_marked_for_liveability.setter
    def is_marked_for_liveability(self, is_marked_for_liveability):
        """Sets the is_marked_for_liveability of this DomainListingAdminServiceV1ModelBusinessProperty.

        Is the property liveability compliant  # noqa: E501

        :param is_marked_for_liveability: The is_marked_for_liveability of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :type: bool
        """

        self._is_marked_for_liveability = is_marked_for_liveability

    @property
    def property_name(self):
        """Gets the property_name of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501

        Name of the property up to 70 characters  # noqa: E501

        :return: The property_name of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this DomainListingAdminServiceV1ModelBusinessProperty.

        Name of the property up to 70 characters  # noqa: E501

        :param property_name: The property_name of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :type: str
        """

        self._property_name = property_name

    @property
    def location(self):
        """Gets the location of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501

        Short location information up to 30 character, e.g.: Greenhills Beach  # noqa: E501

        :return: The location of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this DomainListingAdminServiceV1ModelBusinessProperty.

        Short location information up to 30 character, e.g.: Greenhills Beach  # noqa: E501

        :param location: The location of this DomainListingAdminServiceV1ModelBusinessProperty.  # noqa: E501
        :type: str
        """

        self._location = location

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
        if issubclass(DomainListingAdminServiceV1ModelBusinessProperty, dict):
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
        if not isinstance(other, DomainListingAdminServiceV1ModelBusinessProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other