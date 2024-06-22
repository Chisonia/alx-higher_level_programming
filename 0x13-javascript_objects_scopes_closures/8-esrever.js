#!/usr/bin/node
exports.esrever = function esrever (list) {
  const length = list.length;
  const reversedList = new Array(length);

  for (let i = 0; i < length; i++) {
    reversedList[length - 1 - i] = list[i];
  }

  return reversedList;
};
