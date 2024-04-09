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
      for (let i = 1; i <= this.height; i++) {
          for (let j = 1; i <= this.width; j++)
            console.log(x); 
          }
    }
  }
  module.exports = Rectangle;