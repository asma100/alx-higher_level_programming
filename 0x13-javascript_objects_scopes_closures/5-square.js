#!/usr/bin/node

const Rectangle = require("./4-rectangle");

class Square extends Rectangle(){
  constructor (hight, width, size) {
    super(hight, width);
    this.size = size;
    }
}

module.exports = Square;
module.exports = Rectangle;