#!/usr/bin/node
/* Prints a square */

const input = parseInt(process.argv[2]);
let output = '';
let x;

if (Number.isInteger(input)) {
  for (x = 0; x < input; x++) {
    output += 'X';
  }
  for (x = 0; x < input; x++) {
    console.log(output);
  }
} else {
  console.log('Missing size');
}
