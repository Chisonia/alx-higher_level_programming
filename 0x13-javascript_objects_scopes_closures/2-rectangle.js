#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined || w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {}; // Return empty object if invalid parameters are provided
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
