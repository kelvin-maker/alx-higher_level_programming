#!/usr/bin/node
// Definition of a square (a square is a rectangle)
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
    constructor (size) {
	super(size, size);
    }
};
