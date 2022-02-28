#!/usr/bin/node
// Print a message depending of the number of arguments passed
const messages = ['No argument', 'Argument found', 'Arguments found'];
console.log(messages[Math.min(process.argv.length - 2, 2)]);
