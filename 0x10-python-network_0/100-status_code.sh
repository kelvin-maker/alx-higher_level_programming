#!/bin/bash
# Send a GET request to a URL and display the status code of the response
curl -sL -o /dev/null -w '%{http_code}' -- "$1"
