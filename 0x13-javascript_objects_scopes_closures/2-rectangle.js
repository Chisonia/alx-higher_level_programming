#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w === undefined && h === undefined) {
      // If no arguments provided, return empty Rectangle
      return {};
    } else if (w === undefined || w <= 0 || !Number.isInteger(w)) {
      // If width is undefined, zero, not a positive integer, or not an integer
      return {};
    } else if (h === undefined || h <= 0 || !Number.isInteger(h)) {
      // If height is undefined, zero, not a positive integer, or not an integer
      return {};
    }

    // Assign valid width and height
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
