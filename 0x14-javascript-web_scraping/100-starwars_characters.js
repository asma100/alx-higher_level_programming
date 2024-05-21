#!/usr/bin/node
const request = require('request');

const ID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${ID}/`;

request.get(url, function (err, res, body) {
  if (err) {
    console.error(`Error fetching URL: ${err.message}`);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  for (let i = 0; i < characters.length; ++i) {
    request.get(characters[i], function (err, res, body) {
      if (err) {
        console.error(`Error fetching character URL: ${err.message}`);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  }
});
