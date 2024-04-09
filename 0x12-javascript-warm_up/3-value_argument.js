#!/usr/bin/node
const arg = process.argv[2];
if (arg) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
