#!/usr/bin/node
// Convert a number from base-10 to another base
exports.converter = function (base) {
    return n => n.toString(base);
};
