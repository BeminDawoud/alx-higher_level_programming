#!/usr/bin/node
/*  computes the number of tasks completed by user id. */
const request = require('request');
const url = process.argv[2];
const dict = {};
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    for (const todo of todos) {
      if (todo.completed) {
        if (dict[todo.userId] === undefined) {
          dict[todo.userId] = 0;
        }
        dict[todo.userId]++;
      }
    }
    console.log(dict);
  }
});
