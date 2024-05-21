#!/usr/bin/node
const request = require('request');

function countWedgeAppearances (url) {
  request.get(url, function (_err, _res, body) {
    if (_err) {
      console.error(_err);
      return;
    }

    const films = JSON.parse(body).results;
    const wedgeUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
    let count = 0;

    for (let i = 0; i < films.length; ++i) {
      const characters = films[i].characters;

      for (let j = 0; j < characters.length; ++j) {
        if (characters[j] === wedgeUrl) {
          count++;
          break;
        }
      }
    }

    console.log(count);
  });
}

const filmsUrl = process.argv[2];
countWedgeAppearances(filmsUrl);
