#!/usr/bin/node
const request = require('request');
// Function to make the GET request and display the status code
function getStatusCode (url) {
  if (!url) {
    console.error('Error: Please provide a URL for the GET request.');
    return; // Exit function if no URL is provided
  }
  request.get(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching URL:', error.message);
      return; // Exit callback on error
    }

    console.log(`code: ${response.statusCode}`);
  });
}
// Get the URL from the first argument (process.argv[2])
const url = process.argv[2];
// Call the getStatusCode function
getStatusCode(url);
