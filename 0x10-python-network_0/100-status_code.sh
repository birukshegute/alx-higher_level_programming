#!/bin/bash
# A script that sends a request to a URL passed, and displays only the status code.
curl -L -s -X HEAD -w "%{http_code}" "$1"
