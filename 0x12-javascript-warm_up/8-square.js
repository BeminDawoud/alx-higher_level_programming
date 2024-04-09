#!/usr/bin/node
/* comment */
const arg = parseInt(process.argv[2]);
if (arg) {
  for (let i = 0; i < arg; i++) {
    console.log(Array(arg + 1).join('X'));
  }
} else {
  console.log('Missing size');
}
