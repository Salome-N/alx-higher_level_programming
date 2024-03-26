#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    body = JSON.parse(body);
    const doneTasks = {};
    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      if (completed && !doneTasks[userId]) {
        doneTasks[userId] = 0;
      }
      if (completed) ++doneTasks[userId];
    }
    console.log(doneTasks);
  }
});
