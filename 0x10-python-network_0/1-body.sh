#!/bin/bash
# A script that sends a DELETE request to the URL passed as argument and displays the body
curl -sX GET "$1" -L
