#!/usr/bin/node

if (process.argv.length === 2) {
  console.log('Argument found');
} else if (process.argv.length === 3) {
  console.log('Arguments found');
} else if (process.argv.length === 1) {
  console.log('No argument');
}
