#!/usr/bin/node
// Get the number of tasks completed by user id
const request = require('request');
request(process.argv[2], { json: true }, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else if (body) {
    const tasksByUser = {};
    for (const i in body) {
      if (body[i].completed === true) {
        if (tasksByUser[body[i].userId] === undefined) {
          tasksByUser[body[i].userId] = 1;
        } else {
          tasksByUser[body[i].userId]++;
        }
      }
    }
    console.log(tasksByUser);
  }
});
