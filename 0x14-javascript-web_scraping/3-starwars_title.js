#!/usr/bin/node
const request = require('request');

function getMovieTitle (ID) {
  const url = `https://swapi-api.alx-tools.com/api/films/${ID}`;
  request.get(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const data = JSON.parse(body);
      console.log(data.title);
    } else {
      console.error('Error:', error);
      console.error('Status Code:', response && response.statusCode);
    }
  });
}

const ID = process.argv[2];
getMovieTitle(ID);
