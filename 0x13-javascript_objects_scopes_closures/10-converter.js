#!/usr/bin/node
exports.converter = function converter (base) {
  return function myConverter (number) {
    // Base case: number is less than base
    if (number < base) {
      // Convert to string and handle characters for bases greater than 10
      return number.toString(base).toUpperCase();
    } else {
      // Recursive case: convert quotient and append remainder
      return myConverter(Math.floor(number / base)) + '0123456789abcdefghijklmnopqrstuvwxyz'.charAt(number % base);
    }
  };
};
