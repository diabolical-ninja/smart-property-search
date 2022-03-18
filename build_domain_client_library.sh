#!/bin/bash

echo "Generating client..."

# Location of the Swagger Config
SWAGGER_DOCUMENT="https://developer.domain.com.au/static/latest/media/v1/openapi.json"
CLIENT_NAME="domainClient"

JSON_FMT='{"options":{"packageName": "%s"},"openAPIUrl":"%s"}'
JSON_REQUEST=$(printf "$JSON_FMT" $CLIENT_NAME $SWAGGER_DOCUMENT)

response=$(
    curl -X POST \
        -H "content-type:application/json" \
        -d "$JSON_REQUEST" \
        http://api.openapi-generator.tech/api/gen/clients/python
    )
echo "Generating client...Done"


LINK_URL="$(echo $response | grep -Eo 'http:[^"]+')"

echo "Downloading $CLIENT_NAME..."
curl "$LINK_URL" -o "$CLIENT_NAME.zip"
echo "Downloading $CLIENT_NAME...Done"

echo "Unzip Package $CLIENT_NAME..."
unzip -q $CLIENT_NAME.zip 
echo "Unzip Package $CLIENT_NAME...Done"

mv python-client $CLIENT_NAME
rm -rf $CLIENT_NAME.zip
echo "$CLIENT_NAME library creation done"
