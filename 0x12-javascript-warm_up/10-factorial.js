#!/usr/bin/node
// Print the factorial of an argument
function factorial (x) {
  if (x > 1) {
    return x * factorial(x - 1);
  }
  if (x < 0) {
    return undefined;
  }
  return 1;
}
const n = parseInt(process.argv[2]);
console.log(factorial(n));
