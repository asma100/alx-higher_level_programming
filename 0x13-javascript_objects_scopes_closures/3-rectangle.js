#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
        return this;
      }
      this.width = w;
      this.height = h;
    }
    print(){
      for (let i = 1; i <= h; i++) {
          for (let j = 1; i <= w; j++)
            console.log(j); 
          }
    }
  }
  module.exports = Rectangle;