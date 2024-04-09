#!/usr/bin/node
 class Rectangle {
    constructor (w, h) {
    this.w = w;
    this.h = h;
    if (w <= 0 || h <= 0) {
      this.width = undefined;
      this.height = undefined;
    }


    }
}
module.exports = Rectangle;