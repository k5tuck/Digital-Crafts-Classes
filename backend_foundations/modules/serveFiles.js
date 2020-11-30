const fs = require("fs");

const serveFile = (req, res, filename) => {
  fs.readFile(filename, (err, data) => {
    if (err) {
      res.write(404);
      res.end(err);
    }
    res.write(data);
    res.end();
  });
};

module.exports = serveFile;
