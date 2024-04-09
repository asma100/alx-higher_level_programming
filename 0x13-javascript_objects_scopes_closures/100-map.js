#!/usr/bin/node

const l = require('./100-data.js').l;
console.log(l);
console.log(l.map((item, index) => item * index));