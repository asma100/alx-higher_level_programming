#!/usr/bin/node

const { dict } = require('./101-data');

const occurrencesDict = {};

for (const [userId, occurrences] of Object.entries(dict)) {
    if (occurrences in occurrencesDict) {
        occurrencesDict[occurrences].push(userId);
    } else {

        occurrencesDict[occurrences] = [userId];
    }
}


console.log(occurrencesDict);