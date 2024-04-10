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

  rotate () {
    const tmp = this.width;

    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
