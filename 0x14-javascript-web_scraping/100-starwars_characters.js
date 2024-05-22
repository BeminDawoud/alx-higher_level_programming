#!/usr/bin/node
/*  prints all characters of a Star Wars movie:. */
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const chars = JSON.parse(body).characters;
    for (const char of chars) {
      request(char, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
