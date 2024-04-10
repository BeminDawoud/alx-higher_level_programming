#!/usr/bin/node
/* comment */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      for (let row = 0; row < this.height; row++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}
module.exports = Rectangle;
