#!/usr/bin/node

const request = require('request');

// Check if a movie ID is provided
const movieId = process.argv[2];
if (!movieId) {
	console.log('Usage: ./0-starwars_characters.js <Movie ID>');
	process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/films/${movieId}/`;

request(url, (error, response, body) => {
	if (error) {
		console.log('Error:', error);
		return;
	}

	if (response.statusCode !== 200) {
		console.log('Failed to fetch data. Status Code:', response.statusCode);
		return;
	}

	const movieData = JSON.parse(body);
	const characterUrls = movieData.characters;

	// Iterate over the character URLs and fetch each character's name
	characterUrls.forEach((characterUrl) => {
		request(characterUrl, (charError, charResponse, charBody) => {
			if (charError) {
				console.log('Error fetching character:', charError);
				return;
			}

			if (charResponse.statusCode !== 200) {
				console.log('Failed to fetch character. Status Code:', charResponse.statusCode);
				return;
			}

			const characterData = JSON.parse(charBody);
			console.log(characterData.name);
		});
	});
});
