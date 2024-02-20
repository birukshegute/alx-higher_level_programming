#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/'.concat(episode);

request(url, function (err, res, body) {
  if (err) throw err;
  body = JSON.parse(body);
  console.log(body.title);
});
