#!/usr/bin/node
// Concatenate two files
const fs = require('fs');
try {
    fs.open(process.argv[4], 'w', (err, fd) => {
	if (err) {
	    throw err;
	}
	fs.readFile(process.argv[2], (err, data) => {
	    if (err) {
		throw err;
	    }
	    fs.write(fd, data, (err, bytesWritten, buffer) => {
		if (err) {
		    throw err;
		}
		return bytesWritten;
	    });
	});
	fs.readFile(process.argv[3], (err, data) => {
	    if (err) {
		throw err;
	    }
	    fs.write(fd, data, (err, bytesWritten, buffer) => {
		if (err) {
		    throw err;
		}
		return bytesWritten;
	    });
	});
    });
} catch (err) {
    console.log(err);
}
