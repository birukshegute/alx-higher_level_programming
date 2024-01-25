#!/bin/bash
# A  script that sends a JSON POST request to a URL passed, and displays the body.
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
