# Smart Property Search

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/f69662f84ff54c2ba386c994dd140eb0)](https://www.codacy.com/manual/yeltahir/smart-property-search?utm_source=github.com&utm_medium=referral&utm_content=diabolical-ninja/smart-property-search&utm_campaign=Badge_Grade)      ![Deploy](https://github.com/diabolical-ninja/smart-property-search/workflows/Deploy%20Feature%20Branch/badge.svg)

Buyer focused property search, with results tailored to your needs rather than the agents.

## Client Usage

1.  Build Domain client library

```sh
sh build_domain_client_library.sh
```

2.  Copy contents to `src`

```sh
mv domainClient/domainClient src/domainClient
```

3.  Install & configure serverless via the instructions on their [website](https://www.serverless.com/framework/docs/getting-started/)


4.  Generate client ID & secret from [Domain](https://developer.domain.com.au/docs/introduction) & populate the appropriate fields within `serverless.yml`.

5.  To deploy:

```sh
sls deploy
```

6.  An API will now be available that you can query with different search parameters.

    -   `Domain` [residential search](https://developer.domain.com.au/docs/latest/apis/pkg_agents_listings/references/listings_detailedresidentialsearch)
    -   `Filters` are additional parameters to filter the results

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
        }
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
    }
}
```

7.  Once done, teardown the infrastructure using:

```sh
sls remove
```
