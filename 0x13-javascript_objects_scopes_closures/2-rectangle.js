#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    // Use ternary operator to conditionally initialize attributes
    this.width = (w > 0 && Number.isInteger(w)) ? w : undefined;
    this.height = (h > 0 && Number.isInteger(h)) ? h : undefined;

    // Return an empty object if width or height is invalid
    if (this.width === undefined || this.height === undefined) {
      return {};
    }
  }
}

module.exports = Rectangle;
