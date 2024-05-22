#!/usr/bin/node
/*  prints all characters of a Star Wars movie:. */
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const chars = JSON.parse(body).characters;
    const promises = chars.map(char => makeRequest(char));

    Promise.all(promises)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(error => {
        console.error(error);
      });
  }
});
