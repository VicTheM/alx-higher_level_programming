#!/usr/bin/node
// This script returns the reversed version of a list

exports.esrever = function (list) {
  return list.sort((a, b) => {
    if (typeof a === 'number' && typeof b === 'number') {
      return b - a;
    } else {
      return -1;
    }
  });
};
