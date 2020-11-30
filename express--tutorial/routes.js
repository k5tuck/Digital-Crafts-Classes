const fs = require("fs");

const send404 = fs.readFile("./favicon.ico", (err, data) => {
  if (err) return res.send(`Error: ${err}`);
  res.send(data);
});
