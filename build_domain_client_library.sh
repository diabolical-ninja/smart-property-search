#!/bin/bash

echo "Generating client..."

# Location of the Swagger Config
SWAGGER_DOCUMENT="https://developer.domain.com.au/docs/media/public-adapter-v1.json"
SWAGGER_DOCUMENT="http://petstore.swagger.io/v2/swagger.json"

JSON_FMT='{"options":{"packageName": "domain-client"},"swaggerUrl":"%s"}'
JSON_REQUEST=$(printf "$JSON_FMT" $SWAGGER_DOCUMENT)

response=$(
    curl -X POST \
        -H "content-type:application/json" \
        -d "$JSON_REQUEST" \
        https://generator.swagger.io/api/gen/clients/ruby
    )
echo "Generating client...Done"
echo $response


LINK_URL=$(echo $response | grep -Eo 'https:[^"]+')

CLIENT_NAME="domain-client"
echo "Downloading $CLIENT_NAME..."


curl -X GET $LINK_URL
echo "Downloading $CLIENT_NAME...Done"

echo "Unzip Package $CLIENT_NAME..."
unzip $CLIENT_NAME.zip