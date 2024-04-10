#!/usr/bin/node
// This script concats 2 files.

const fs = require('fs');

const fileA = fs.readFileSync(process.argv[2], 'utf-8');
const fileB = fs.readFileSync(process.argv[3], 'utf-8');
const fileC = process.argv[4];

fs.appendFileSync(fileC, fileA);
fs.appendFileSync(fileC, fileB);
