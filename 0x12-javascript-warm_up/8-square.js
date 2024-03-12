#!/usr/bin/node
/* Prints a square */

let input = parseInt(process.argv[2])
let output = ""

if (Number.isInteger(input)) {
	for (let x = 0; x < input; x++) {
		output += 'X'
	}
	for (x = 0; x < input; x++) {
		console.log(output)
	}
} else {
	console.log('Missing size')
}
