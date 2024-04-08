#!/usr/bin/node
// This script prints “C is fun” x times

const x = parseInt(process.argv[2]);

if (x) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
