#!/usr/bin/node
/* in-fixes a string between two strings */

let str1 = process.argv[2]
let str2 = process.argv[3]

if (!str1) {
  str1 = 'undefined'
}
if (!str2) {
  str2 = 'undefined'
}
console.log(str1.concat(' is ', str2))
