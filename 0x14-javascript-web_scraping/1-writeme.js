#!/usr/bin/node
const fs = require('fs');
// Function to write a string to a file
function writeStringToFile (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', function (err) {
    if (err) {
      console.error(`Error writing to file: ${err.message}`);
    }
  });
}
const filePath = process.argv[2];
const content = process.argv[3];
writeStringToFile(filePath, content);
