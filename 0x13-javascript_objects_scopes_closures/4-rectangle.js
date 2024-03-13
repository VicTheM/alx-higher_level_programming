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

  // Another public instance method
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  // Yet another public method
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
