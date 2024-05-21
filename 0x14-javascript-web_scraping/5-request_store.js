#!/usr/bin/node
const request = require('request');
const fs = require('fs');

function storeWebpage (url, filePath) {
  request.get(url, function (_err, _res, body) {
    if (_err) {
      console.error(`Error fetching URL: ${_err.message}`);
      return;
    }

    fs.writeFile(filePath, body, 'utf-8', function (err) {
      if (err) {
        console.error(`Error writing to file: ${err.message}`);
      }
    });
  });
}

const url = process.argv[2];
const filePath = process.argv[3];
storeWebpage(url, filePath);
