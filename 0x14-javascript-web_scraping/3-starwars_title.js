#!/usr/bin/node

const request = require('request');
let sturl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(sturl, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
