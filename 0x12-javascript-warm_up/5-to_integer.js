#!/usr/bin/node
/* comment */
const args = process.argv.length;
if (parseInt(args[3])) {
  console.log('My number:', parseInt(args[3]));
}
else {
  console.log('Not a number');
}
