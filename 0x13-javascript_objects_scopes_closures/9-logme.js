#!/usr/bin/node
// Print the number of arguments already printed and the new argument
exports.logMe = function (item) {
    if (this.n_printed === undefined) {
	this.n_printed = 0;
    }
    console.log(this.n_printed++ + ': ' + item);
};
