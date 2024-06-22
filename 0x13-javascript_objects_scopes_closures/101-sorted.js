#!/usr/bin/node

const dict = require('./101-data').dict;

const occurrencesByIds = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (occurrences in occurrencesByIds) {
    occurrencesByIds[occurrences].push(userId);
  } else {
    occurrencesByIds[occurrences] = [userId];
  }
}

console.log(occurrencesByIds);
