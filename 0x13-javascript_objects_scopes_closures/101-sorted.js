#!/usr/bin/node
/* comment */
const { dict } = require('./101-data');
const newDict = Object.entries(dict).reduce((acc, [userId, occurrences]) => {
  acc[occurrences] = acc[occurrences] ? [...acc[occurrences], userId] : [userId];
  return acc;
}, {});

console.log(newDict);
