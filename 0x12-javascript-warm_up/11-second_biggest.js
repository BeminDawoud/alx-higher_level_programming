#!/usr/bin/node
/* comment */
const len = process.argv.length;
if (len === 2) {
  console.log(0);
} else if (len === 3) {
  console.log(0);
} else {
  const arr = process.argv.slice(2).sort();
  console.log(arr[arr.length - 2]);
}
