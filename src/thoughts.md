
# API Gameplan

1. Get all properties based on initial search criteria
2. For all returned, get travel time & distance from "destination location"
3. Filter all returned based on travel time filer (eg <=25min)
4. For remaining listings, get their full fat add description
5. Apply "smart filters" based on the results
    - keyword searches such as aircon, dishwasher, etc
    - extended searches such as NBN


# API Design

```json
{
    "domainParameters": {},
    "smartFilters": {
        "nbn": "<type>",
        "travelTime": {
            "destinationAddress": "123 abc st",
            "maxTravelTime": 55 //minutes
        },
        "airconditioning": true
    }
}

```


## Response

```json
{
    "num_beds": 1,
    "num_baths": 1, 
    "num_paths": 1,
    "property_type": 1,
    "address": 1,
    "distance from destination" 1,
    "duration from destination" 1,
    "distance from destination" 1
    }


```