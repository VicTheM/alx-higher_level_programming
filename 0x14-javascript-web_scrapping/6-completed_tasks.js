#!/usr/bin/node
// This script computes the number of tasks completed by user id.

const request = require('request');

request(process.argv[2],
  (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const data = JSON.parse(body);
      const users = {};

      for (const todo of data) {
        if (todo.completed) {
          const userId = todo.userId;

          if (users[userId]) {
            users[userId]++;
          } else {
            users[userId] = 1;
          }
        }
      }
      console.log(users);
    }
  });
