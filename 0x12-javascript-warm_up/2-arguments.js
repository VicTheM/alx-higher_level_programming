#!/usr/bin/node
// Reads command line argumemts

let args = process.argv;
let len = args.length;
if (len <= 2) {
	console.log(`No argument`);
}
else if (len === 3) {
	console.log(`Argument found`);
}
else {
	console.log(`Arguments found`);
}
