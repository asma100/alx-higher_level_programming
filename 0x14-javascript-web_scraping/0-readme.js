#!/usr/bin/node
const fs = require('fs');

// Function to read and print file content
function readFile (filePath) {
  if (!filePath) {
    console.error('Error: Please provide a file path as the first argument.');
    return; // Exit function if no path is provided
  }

  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(`Error reading file: ${err.message}`);
      return; // Exit callback on error
    }

    console.log(data);
  });
}

// Get the file path from the first argument (process.argv[2])
const filePath = process.argv[2];

// Call the readFile function with the extracted path
readFile(filePath);
