#!/usr/bin/node
// This script increments and calls a function

exports.addMeMaybe = function (number, theFunction) {
  number += 1;
  theFunction(number);
};
