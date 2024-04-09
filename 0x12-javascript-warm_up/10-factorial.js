#!/usr/bin/node
/* comment */
function factorial (num) {
  if (num === 1) {
    return (1);
  }
  return num * factorial(num - 1);
}
const arg = parseInt(process.argv[2]);
if (arg) {
  console.log(factorial(arg));
} else {
  console.log(1);
}
