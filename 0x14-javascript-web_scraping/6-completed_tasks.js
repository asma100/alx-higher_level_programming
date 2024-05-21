#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.error(`Error fetching URL: ${err.message}`);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasks = {};

  for (let i = 1; i <= todos.length; i++) {
    let count = 0;
    for (let j = 0; j < todos.length; j++) {
      if (todos[j].userId === i && todos[j].completed) {
        count++;
      }
    }
    if (count > 0) {
      completedTasks[i] = count;
    }
  }

  console.log(completedTasks);
});
