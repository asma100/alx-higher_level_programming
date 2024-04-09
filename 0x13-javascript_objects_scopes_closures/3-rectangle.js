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
          let row = '';
          for (let j = 1; i <= this.width; j++)
            row += 'X';
            console.log('X'); 
          }
    }
  }
  module.exports = Rectangle;