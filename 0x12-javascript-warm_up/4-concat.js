#!/usr/bin/node
let first = 'undefined';
let second = 'undefined';
if (process.argv[1]) {
  first = process.argv[1];
}
if (process.argv[2]) {
  second = process.argv[2];
}
console.log(`${first} is ${second}`);
