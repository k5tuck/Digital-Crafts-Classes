const fs = require("fs");
let lockfile = false;
const writeFile = () => {
  if (!lockfile) {
    lockfile = true;
  } else {
    console.log("File is locked");
  }
};
