#!/usr/bin/node
// Find the second greatest integer given as an argument
const numbers = process.argv.slice(2).map(x => parseInt(x));
if (numbers.length < 2) {
  console.log(0);
} else {
  console.log([...new Set(numbers)].sort((a, b) => b - a)[1]);
}
