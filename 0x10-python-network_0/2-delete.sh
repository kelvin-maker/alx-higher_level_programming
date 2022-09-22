#!/bin/bash
# Send a DELETE request to a URL and display the body of the response
curl -sL -X DELETE -- "$1"
