#!/usr/bin/node
/* display the status code of a GET request. */
const request = require('request');
let count = 0;
const actor = 'https://swapi-api.alx-tools.com/api/people/18/';
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    for (const film of films) {
      if (film.characters.includes(actor)) {
        count++;
      }
    }
    console.log(count);
  }
});
