#!/usr/bin/node
/* comment */
exports.esrever = function (list) {
  const temp = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    temp[i] = list[j];
    j++;
  }
  return (temp);
};
