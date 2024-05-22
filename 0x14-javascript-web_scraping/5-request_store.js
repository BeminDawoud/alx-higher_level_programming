#!/usr/bin/node
/*  gets the contents of a webpage and stores it in a file. */
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(fileName, body, error => {
      if (error) {
        console.log(error);
      }
    });
  }
});
