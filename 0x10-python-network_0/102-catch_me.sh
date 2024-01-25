#!/bin/bash
# A script that requests 0.0.0.0:5000/catch_me and responds with "You got me!"
curl -s -L -X PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me
