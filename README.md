# Smart Property Search

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/f69662f84ff54c2ba386c994dd140eb0)](https://www.codacy.com/manual/yeltahir/smart-property-search?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=diabolical-ninja/smart-property-search&amp;utm_campaign=Badge_Grade)

Buyer focused property search, with results tailored to your needs rather than the agents.


# Process

1. Build Domain client library
```sh
sh build_domain_client_library.sh
```

2. Install library
```sh
cd domainClient
python setup.py install
```

3. To use the library, first generate an access token:

```python
# Import both API client & authentication fn
import domainClient as dc
from src.domain_authentication import get_access_token

# Populate Keys & Scope
client_id = '<client id>'
client_secret = '<client secret>'
scopes = ['api_listings_read', 'api_agencies_read'] # Extend/Update as required

# Generate Access Token
auth_info = get_access_token(client_id, client_secret, scopes)
print(auth_info)
```

4. It can then by used to interact with the API. For all methods see:
    https://developer.domain.com.au/docs/apis

```python
# Configure Authentication Client
configuration = dc.Configuration()
configuration.access_token = auth_info['access_token']

# View most recent sales results in Adelaide
sales_results_obj = dc.SalesResultsApi(dc.ApiClient(configuration))
sales_results_obj.sales_results_listings('Adelaide')
```