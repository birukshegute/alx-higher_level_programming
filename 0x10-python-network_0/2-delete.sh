#!/bin/bash
# script that sends a DELETE request to the URL passed and displays the body
curl -s -X DELETE "$1"
