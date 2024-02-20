#!/usr/bin/node

const fs = require('fs');
const text = process.argv[3];
const path = process.argv[2];

fs.writeFile(path, text, 'utf8', (err) => {
  if (err) throw err;
});
