#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request(url, function (err, res, body) {
  if (err) throw err;
  fs.writeFile(path, body, 'utf8', (err) => {
    if (err) throw err;
  });
});
