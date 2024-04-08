#!/usr/bin/env node
// Ask user for input


let myName;
do {
	myName = prompt("Enter your name: ");
} while (!myName);

console.log(myName);
