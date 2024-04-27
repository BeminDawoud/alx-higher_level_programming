#!/bin/bash
#displays the size of the body of the response
curl -s -L -X GET -H "X-School-User-Id: 98" "$1"
