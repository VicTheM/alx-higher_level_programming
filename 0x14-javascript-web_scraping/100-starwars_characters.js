#!/usr/bin/node
// This script prints all characters of a Star Wars movie.

const request = require('request');

const id = process.argv[2];
request(`https://swapi-api.alx-tools.com/api/films/${id}`,
  (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const data = JSON.parse(body);

      data.characters.forEach((character) => {
        request(character, (error, response, body) => {
          if (error) {
            console.log(error);
          } else {
            const data = JSON.parse(body);

            console.log(data.name);
          }
        });
      });
    }
  });
