#!/usr/bin/node
// Convert the first argument to an integer
const number = parseInt(process.argv[2]);
if (Number.isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
