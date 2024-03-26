#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let n = 0;

request(url, function (err, res, body) {
  result = JSON.parse(body).results;
  for (let l = 0; l < result.length; ++l) {
    const chars = result[l].characters;
    for (let ln = 0; ln < chars.length; ++ln) {
      const c = chars[ln];
      const charId = c.split('/')[5];
      if (charId === '18') {
	n += 1;
      }
    }
  }
  
  console.log(n);
});
