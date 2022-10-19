#!/usr/bin/node
// READ FIle

//requre fs
const fs = require('fs')

//Reading data in utf-8 format
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
    if (err) throw err;
    
    console.log(data);
})
