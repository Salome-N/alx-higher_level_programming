#!/usr/bin/node

const request = require('request');
const fs = require('fs');
request(process.argv[2], function (_error, response, body) {
  fs.writeFile(process.argv[3], body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
