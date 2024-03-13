#!/usr/bin/node
/* Defines a class */

class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Public instance method
  print () {
    let x;
    let output = '';
  	for (x = 0; x < this.width; x++) {
      output += 'X';
  	}
    for (x = 0; x < this.height; x++) {
      console.log(output);
    }
  }
}
module.exports = Rectangle;
