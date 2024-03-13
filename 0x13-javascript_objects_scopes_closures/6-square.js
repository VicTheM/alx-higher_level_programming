#!/usr/bin/node
/* Defines a class */

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (k) {
	  let x;
	  let out = '';
	  let letter;
	  if (k) {
      letter = k;
	  } else {
      letter = 'X';
	  }

	  for (x = 0; x < this.width; x++) {
      out += letter;
	  }
	  for (x = 0; x < this.height; x++) {
		  console.log(out);
	  }
  }
}

module.exports = Square;
