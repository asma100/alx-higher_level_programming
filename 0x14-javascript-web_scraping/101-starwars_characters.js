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
  const characterNames = Array(characters.length).fill(null);
  let count = 0;

  for (let i = 0; i < characters.length; ++i) {
    request.get(characters[i], function (err, res, body) {
      if (err) {
        console.error(`Error fetching character URL: ${err.message}`);
        return;
      }

      const character = JSON.parse(body);
      characterNames[i] = character.name;
      count++;

      // Check if all characters have been fetched
      if (count === characters.length) {
        for (let j = 0; j < characterNames.length; ++j) {
          console.log(characterNames[j]);
        }
      }
    });
  }
});
