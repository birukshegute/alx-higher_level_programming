##!/bin/bash
# A script that takes in a URL, sends a POST request, and displays the body.
curl -s -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" -X POST "$1"
