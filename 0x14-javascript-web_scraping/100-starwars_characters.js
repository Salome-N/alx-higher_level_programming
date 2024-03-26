#!/usr/bin/node

const request = require('request');
const swurl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(swurl, function (_err, res, body) {
  const chars = JSON.parse(body).characters;
  chars.forEach((c) => {
    request(c, function (_err, res, body) {
      console.log(JSON.parse(body).name);
    });
  });
});
