#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let l = 0; l < this.height; l++) console.log(c.repeat(this.width));
    }
  }
};
