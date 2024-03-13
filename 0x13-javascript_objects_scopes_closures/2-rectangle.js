#!/usr/bin/node
/* Defines a class */

class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w
      this.height = h
    }
  }
}
module.exports = Rectangle
