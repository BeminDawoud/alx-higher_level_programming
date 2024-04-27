#!/bin/bash
#displays the size of the body of the response
curl -sI -L -X OPTIONS "$1" | grep Allow | sed 's/Allow: //I'
