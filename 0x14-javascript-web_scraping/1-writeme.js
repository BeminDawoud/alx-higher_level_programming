#!/usr/bin/node
/* writes content to a file */
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], (error) => {
  if (error) {
    console.error(error);
  }
});
