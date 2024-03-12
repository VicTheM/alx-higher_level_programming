#!/usr/bin/node
/* Scopes - Bindings - Closure */

const mine = function (x, theFunction) {
  let c = x
  while (c > 0) {
    theFunction()
    c--
  }
}

exports.callMeMoby = mine
