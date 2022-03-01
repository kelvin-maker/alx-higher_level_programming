#!/usr/bin/node
// Print the first argument if provided
if (process.argv[2] !== undefined) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
