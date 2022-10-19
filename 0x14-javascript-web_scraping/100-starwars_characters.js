#!/usr/bin/node
// Print all characters of a Star Wars movie
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(url, { json: true }, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else if (body) {
    const characters = body.characters;
    for (const i in characters) {
      request(characters[i], { json: true }, (err, resp, body) => {
        if (err) {
          console.log(err);
        } else if (body) {
          console.log(body.name);
        }
      });
    }
  }
});
