#!/usr/bin/node
/* comment */
const squareParent = require('./5-square');

class Square extends squareParent {
  charPrint (c = 'X') {
    if (this.width && this.height) {
      for (let row = 0; row < this.height; row++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
