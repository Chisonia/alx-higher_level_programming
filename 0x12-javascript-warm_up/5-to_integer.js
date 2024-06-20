#!/usr/bin/node

const arg = process.argv[2];
const conv = parseInt(arg, 10);

if (isNaN(conv)) {
  console.log('Not a number');
} else {
  console.log('My number: %d', conv);
}
