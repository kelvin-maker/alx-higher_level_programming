#!/usr/bin/node
// Print a square of height x
const x = parseInt(process.argv[2]);
if (Number.isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i += 1) {
    console.log('X'.repeat(x));
  }
}
