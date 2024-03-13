#!/usr/bin/node
// This script creates a class Square that defines a square and inherits from Rectangle

const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let breath = '';
      for (let j = 0; j < this.width; j++) {
        breath += c;
      }
      console.log(breath);
    }
  }
}

module.exports = Square;
