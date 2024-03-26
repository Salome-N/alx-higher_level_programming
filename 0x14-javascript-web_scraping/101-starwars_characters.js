#!/usr/bin/node

const request = require('request');
const swurl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(swurl, function (_err, _res, body) {
  const chars = JSON.parse(body).characters;
  printchars(chars, 0);
});

function printchars (chars, i) {
  request(chars[i], function (_err, _res, body) {
    console.log(JSON.parse(body).name);
    if (i + 1 < chars.length) {
      printchars(chars, i + 1);
    }
  });
}
