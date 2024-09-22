#!/usr/bin/node
// This script prints all characters of a Star Wars movie.

const request = require('request');

const id = process.argv[2];

async function makeSyncRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode === 200) {
        resolve(body);
      } else {
        reject(new Error(`Request failed with status code ${response.statusCode}`));
      }
    });
  });
}

async function main (id) {
  try {
    const response = await makeSyncRequest(`https://swapi-api.alx-tools.com/api/films/${id}`);
    const characters = JSON.parse(response).characters;
    for (const character of characters) {
      const response = await makeSyncRequest(character);
      const data = JSON.parse(response);
      console.log(data.name);
    }
  } catch (error) {
    console.log(error);
  }
}

main(id);
