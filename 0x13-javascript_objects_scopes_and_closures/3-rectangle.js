#!/usr/bin/node
// This script creates a class Rectangle that defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let breath = '';
      for (let j = 0; j < this.width; j++) {
        breath += 'X';
      }
      console.log(breath);
    }
  }
}

module.exports = Rectangle;
