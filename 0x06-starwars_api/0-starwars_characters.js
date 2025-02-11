#!/usr/bin/node

function makeRequest (url) {
	const request = require('request');
	return new Promise((resolve, reject) => {
		request.get(url, (error, response, body) => {
			if (error) reject(error);
			else resolve(JSON.parse(body));
		});
	});
}

async function main () {
	const args = process.argv;

	if (args.length < 3) return;
	const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
	const movie = await makeRequest(movieUrl);

	if (movie.characters === undefined) return;
	for (const characterUrl of movie.characters) {
		const character = await makeRequest(characterUrl);
		console.log(character.name);
	}
}

main();
