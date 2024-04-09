#!/usr/bin/node
 class Rectangle {
    constructor (w, h) {
    this.width = w;
    this.height = h;
    if (width <= 0 || height <= 0) {
      this.width = undefined;
      this.height = undefined;
    }

    }
}
module.exports = Rectangle;