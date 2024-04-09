#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
        return this;
      }
      this.width = w;
      this.height = h;
    }
  
    print () {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'X';
        }
        console.log(row);
      }
    }
    rotate(){
      let x = this.height;
      this.height = this.width;
      this.width = x;

    }
    double(){
      this.height = this.height * this.height;
      this.width = this.width * this.width;
    }
  }
  
  module.exports = Rectangle;