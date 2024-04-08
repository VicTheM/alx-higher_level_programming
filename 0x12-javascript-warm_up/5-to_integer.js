#!/usr/bin/node
/* converts string to integer */

const input = parseInt(process.argv[2]);
if (Number.isInteger(input)) {
  console.log(`My number: ${input}`);
} else {
  console.log('Not a number');
}
