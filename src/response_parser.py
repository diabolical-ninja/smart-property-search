"""Functions to clean up output for API response."""


def clean_response(listing: dict) -> dict:
    """Main function to collect & clean details for API return.

    Args:
        listing (dict): Full SmartSearch search results

    Returns:
        dict: Cleaned details for response
    """
    return {
        "listing": clean_domain(listing["listing"]),
        "travel_details": clean_travel_info(listing.get("travel_info", {})),
        "nbn": listing.get("nbn_details", {}).get("addressDetail", {}).get("techType", None),
        "walkscore": clean_walkscore(listing.get("walkscore", {})),
    }


def clean_domain(listing: dict) -> dict:
    """Extracts key listing details for API return.

    Args:
        listing (dict): Domain listing object

    Returns:
        dict: Address, property details, price & some ID info
    """
    address = {
        "displayable_address": listing.get("property_details", {}).get(
            "displayable_address", ""
        ),
        "postcode": listing.get("property_details", {}).get("postcode", ""),
        "state": listing.get("property_details", {}).get("state", ""),
    }

    property_details = {
        "property_type": listing.get("property_details", {}).get("property_type", ""),
        "features": listing.get("property_details", {}).get("features", []),
        "bathrooms": listing.get("property_details", {}).get("bathrooms", None),
        "bedrooms": listing.get("property_details", {}).get("bedrooms", None),
        "carspaces": listing.get("property_details", {}).get("carspaces", None),
    }

    return {
        "id": listing.get("id", None),
        "listing_slug": listing.get("listing_slug", ""),
        "price": listing.get("price_details", {}).get("display_price", ""),
        "address": address,
        "property_details": property_details,
    }


def clean_travel_info(travel_details: dict) -> dict:
    """Extracts & prepares the travel time information.

    Converts:
        - Metres to kilometres
        - Seconds to minutes

    Args:
        travel_details (dict): Raw travel info

    Returns:
        dict: Travel info in human friendly units
    """
    if travel_details == {} or travel_details["distance"] == "No Result":
        distance = "No Result"
    else:
        distance_in_km = travel_details["distance"] / 1000
        distance = f"{round(distance_in_km, 2)}km"

    if travel_details == {} or travel_details["duration"] == "No Result":
        travel_time = "No Result"
    else:
        duration_in_mins = travel_details["duration"] / 60
        travel_time = f"{round(duration_in_mins, 2)}mins"

    return {"distance": distance, "travel_time": travel_time}


def clean_walkscore(walkscore_details: dict) -> dict:
    """Extracts the desired walkscore information for API return.

    Args:
        walkscore_details (dict): Collected walkscore payload

    Returns:
        dict: Key items desired from walkscore
    """
    return {
        "walkscore": walkscore_details.get("walkscore", None),
        "summary": walkscore_details.get("description", ""),
        "transit": walkscore_details.get("transit", {}),
    }
