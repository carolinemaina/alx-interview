#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Get the movie ID from the command-line argument

const url = `https://swapi.dev/api/films/${movieId}/`; // Construct the API URL for the movie

// Send a GET request to fetch movie data
request(url, function (error, response, body) {
  if (error) {
    console.log('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters; // Get the list of character URLs

    // Iterate over each character URL
    characterUrls.forEach(function (characterUrl) {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.log('Error:', error);
          return;
        }

        if (response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name); // Print the character's name
        }
      });
    });
  } else {
    console.log('Failed to retrieve movie data');
  }
});

