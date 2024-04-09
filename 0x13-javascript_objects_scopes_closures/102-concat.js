#!/usr/bin/node

const files = require('files');
const f1 = files.readFileSync(process.argv[2], 'utf8');
const f2 = files.readFileSync(process.argv[3], 'utf8');
files.writeFileSync(process.argv[4], f1 + f2);