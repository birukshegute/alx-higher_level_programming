#!/bin/bash
# A script that takes in a URL as an argument, sends a GET request, and displays the body
curl -s -H "X-School-User-Id: 98" "$1"
