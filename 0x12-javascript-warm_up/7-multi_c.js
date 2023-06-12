#!/usr/bin/node

const occurences = Number(process.argv[2]);
if (occurences) {
  for (let x = 0; x < occurences; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
