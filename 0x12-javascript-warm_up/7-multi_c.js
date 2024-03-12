#!/usr/bin/node
/* receives control from cmd */

let input = parseInt(process.argv[2])
if (Number.isInteger(input)) {
	for (let x = 0; x < input; x++) {
		console.log('C if fun')
	}
} else {
	console.log('Missing number of occurences')
}
