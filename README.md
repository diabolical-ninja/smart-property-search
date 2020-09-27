# Smart Property Search

![Linting](https://github.com/diabolical-ninja/smart-property-search/workflows/Linting/badge.svg) ![Deploy](https://github.com/diabolical-ninja/smart-property-search/workflows/Deploy%20Feature%20Branch/badge.svg) [![codecov](https://codecov.io/gh/diabolical-ninja/smart-property-search/branch/master/graph/badge.svg)](https://codecov.io/gh/diabolical-ninja/smart-property-search)



Buyer focused property search, with results tailored to your needs rather than the agents.

## How to Build & Deploy the API

Assumes you have:

- An AWS Account including access & secret keys
- Domain client ID & secret, available from [Domain](https://developer.domain.com.au/docs/introduction) 
- A Google maps API key
- WalkScore API key, available from [Walk Score](https://www.walkscore.com/professional/walk-score-apis.php)

1.  Build Domain client library

```sh
sh build_domain_client_library.sh
```

2.  Copy contents to `src`

```sh
mv domainClient/domainClient src/domainClient
```

3.  Install & configure serverless via the instructions on their [website](https://www.serverless.com/framework/docs/getting-started/)

4. Populate `serverless.yml` with all required keys


5.  To deploy:

```sh
sls deploy
```


6.  Once done, teardown the infrastructure using:

```sh
sls remove
```

## Using the API

An API will now be available that you can query with different search parameters. 

To query the API make a `POST` request using your favourite client & include a `JSON` body with your search & filter criteria. The key items to include are:

-   `Domain` [residential search](https://developer.domain.com.au/docs/latest/apis/pkg_agents_listings/references/listings_detailedresidentialsearch)
-   `Filters` are (optional) additional parameters to filter the results


Currently the supported filters are:
* `travelTime`
    - A desired destination & the maximum allowable public transport time to get there
* `features`
    - List of features the property must have:
        - AirConditioning
        - Heating
        - Outside
        - Dishwasher
    - Also see `src/filter_parameters.yml`
* `nbn`
    - List of desired NBN types from [NBN technologies](https://www.nbnco.com.au/learn/network-technology)
* `walkscore`
    - Minimum allowable walkscore value, as defined by [Walk Score](https://www.walkscore.com/)


Full deatils or requests & the acceptable parameters are available in `search_schema.json`


A request will look like:

```json
{
    "domain":{
        // as per domain docs
    },
    "filters":{
        "travelTime": {
            "destinationAddress": "<target destination>",
            "maxTravelTime": 10 //minutes
        },
        "features":["<keys from feature_parameters.yml>", ],
        "nbn": ["<list of nbn types>"],
        "walkscore": <minimum allowable walkscore>
    }
}
```

Eg:

```json
{
    "domain": {
        "listingType": "Sale",
        "propertyTypes": ["Penthouse","ApartmentUnitFlat"],
        "minBedrooms": 4,
        "minBathrooms": 3,
        "minPrice": 4500000,
        "locations": [{
            "state": "VIC",
            "postcode": "3000"
        }
        ]
    },
    "filters": {
       "travelTime": {
            "destinationAddress": "Spring St, East Melbourne VIC 3002",
            "maxTravelTime": 20 //minutes
        }
    },
    "features":["AirConditioning", "Outside"],
    "nbn": ["FTTP", "FTTB", "FTTC"],
    "walkscore": 75
}
```
