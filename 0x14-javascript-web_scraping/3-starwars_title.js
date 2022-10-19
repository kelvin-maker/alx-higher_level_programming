#!/usr/bin/node
// Print the title of the Star Wars movie matching the given number
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(url, { json: true }, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else if (body) {
    console.log(body.title);
  }
});
