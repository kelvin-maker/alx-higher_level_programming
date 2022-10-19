#!/usr/bin/node
// Make a GET request and print the status code
const request = require('request');
request(process.argv[2], (err, resp, body) => {
  if (err) {
    console.log(err);
  } else if (resp) {
    console.log(`code: ${resp.statusCode}`);
  }
});
