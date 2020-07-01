# Smart Property Search

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/f69662f84ff54c2ba386c994dd140eb0)](https://www.codacy.com/manual/yeltahir/smart-property-search?utm_source=github.com&utm_medium=referral&utm_content=diabolical-ninja/smart-property-search&utm_campaign=Badge_Grade)

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

6.  An API will now be up that you can query with different search parameters as per the [residential search](https://developer.domain.com.au/docs/latest/apis/pkg_agents_listings/references/listings_detailedresidentialsearch) docs on domain. Eg:
```json
{
    "listing_type": "Sale",
    "minBedrooms": 2,
    "maxBathrooms": 4,
    "minCarspaces": 1,
    "minPrice": 500000,
    "locations": [{
        "state": "SA"
    }],
    "pageSize": 100
}
```

7.  Once done, teardown the infrastructure using:
```
sls remove
```