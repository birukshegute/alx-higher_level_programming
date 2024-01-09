#!/usr/bin/node
// prints 'C is fun' x times

const line = 'C is fun';

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(line);
  }
}
