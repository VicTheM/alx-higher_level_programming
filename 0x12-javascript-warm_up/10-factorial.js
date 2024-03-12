#!/usr/bin/node
/* computes Factorial */

function factorial (num) {
  if (!num) {
    return 1
  }
  return num * factorial(num - 1)
}

console.log(factorial(parseInt(process.argv[2])))
