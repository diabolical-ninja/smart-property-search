#!/bin/bash

echo "Generating client..."

# Location of the Swagger Config
SWAGGER_DOCUMENT="https://developer.domain.com.au/docs/media/public-adapter-v1.json"

JSON_FMT='{"options":{"packageName": "domain-client"},"swaggerUrl":"%s"}'
JSON_REQUEST=$(printf "$JSON_FMT" $SWAGGER_DOCUMENT)

response=$(
    curl -X POST \
        -H "content-type:application/json" \
        -d "$JSON_REQUEST" \
        https://generator.swagger.io/api/gen/clients/python
    )
echo "Generating client...Done"


LINK_URL=$(echo $response | grep -Eo 'https:[^"]+')
CLIENT_NAME="domain-client"

echo "Downloading $CLIENT_NAME..."
curl $LINK_URL -o $CLIENT_NAME.zip
echo "Downloading $CLIENT_NAME...Done"

echo "Unzip Package $CLIENT_NAME..."
unzip $CLIENT_NAME.zip -q
echo "Unzip Package $CLIENT_NAME...Done"

mv python-client $CLIENT_NAME
rm -rf $CLIENT_NAME.zip
echo "$CLIENT_NAME library creation done"
