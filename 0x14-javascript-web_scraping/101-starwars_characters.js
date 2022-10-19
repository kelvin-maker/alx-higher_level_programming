#!/usr/bin/node
// Print all characters of a Star Wars movie
const request = require('request');
const url = 'https://swapi.co/api/films';
request(url, { json: true }, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else if (body) {
    for (const i in body.results) {
      if (body.results[i].url.endsWith(`/${process.argv[2]}/`)) {
        const characters = body.results[i].characters;
        (func, ...args) { 
        for (const j in characters) {
          request(characters[j], { json: true }, (err, resp, body) => {
            if (err) {
              console.log(err);
            } else if (body) {
              console.log(body.name);
            }
          });
        }
      }
    }
  }
});
