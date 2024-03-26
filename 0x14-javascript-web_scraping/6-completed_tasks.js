#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
      todos = JSON.parse(body);
      const doneTasks = {};
      for (let i = 0; i < todos.length; ++i) {
	const userId = todos[i].userId;
	const completed = todos[i].completed;

	if (completed && !doneTasks[userId]) {
           doneTasks[userId] = 0;
	}
	if (completed) ++doneTasks[userId];
      }
      console.log(doneTasks);
  }
});
