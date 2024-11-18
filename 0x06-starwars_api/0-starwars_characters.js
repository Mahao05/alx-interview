#!/usr/bin/node

const axios = require('axios');

const fetchCharacters = async (movieId) => {
    const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';

    try {
        const movieResponse = await axios.get(`${baseUrl}${movieId}/`);
        const movieData = movieResponse.data;

        console.log(`Characters in '${movieData.title}':`);

        for (const characterUrl of movieData.characters) {
            try {
                const characterResponse = await axios.get(characterUrl);
                console.log(characterResponse.data.name);
            } catch (error) {
                console.error(`Error fetching character data: ${error.message}`);
            }
        }
    } catch (error) {
        console.error(`Error fetching movie data: ${error.message}`);
    }
};

const main = () => {
    const args = process.argv.slice(2);

    if (args.length !== 1) {
        console.log('Usage: node script.js <Movie ID>');
        process.exit(1);
    }

    const movieId = args[0];
    if (isNaN(movieId)) {
        console.log('Movie ID must be a number.');
        process.exit(1);
    }

    fetchCharacters(movieId);
};

main();
