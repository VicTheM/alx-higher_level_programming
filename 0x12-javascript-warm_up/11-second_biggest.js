#!/usr/bin/node
// This script searches the second biggest integer in the list of arguments

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const array = process.argv.slice(2);

  array.sort((a, b) => b - a);
  console.log(array[1]);
}
