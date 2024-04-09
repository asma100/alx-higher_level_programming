#!/usr/bin/node

if (process.argv.length === 2) {
  console.log('Argument found');
} else if (process.argv.length > 2) {
  console.log('Arguments found');
} else if(process.argv.length < 2) {
  console.log('No argument');
}
