#!/usr/bin/node
/* comment */
const args = process.argv;
if (parseInt(args[2])) {
  console.log('My number:', parseInt(args[2]));
} else {
  console.log('Not a number');
}
