#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line argument
const movieId = process.argv[2];

// Make the request to the Star Wars API for the specific movie
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (err, response, body) => {
	if (err) {
		console.log('Error:', err);
		return;
	}

	// Parse the response body (JSON data)
	const data = JSON.parse(body);

	// If the movie ID is invalid, return an error message
	if (!data.title) {
		console.log('Movie not found');
		return;
	}

	// Get the characters list from the movie data
	const characters = data.characters;

	// For each character URL, make a request to get the character details
	characters.forEach((characterUrl) => {
		request(characterUrl, (err, response, body) => {
			if (err) {
				console.log('Error:', err);
				return;
			}

			const characterData = JSON.parse(body);
			console.log(characterData.name);
		});
	});
});
