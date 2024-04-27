#!/bin/bash
#displays the size of the body of the response
curl -si "$1" | grep -i "content-length" | awk '{print $2}'
