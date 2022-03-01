#!/usr/bin/node
// Print 'C is fun' x times
const x = parseInt(process.argv[2]);
if (Number.isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i += 1) {
    console.log('C is fun');
  }
}
