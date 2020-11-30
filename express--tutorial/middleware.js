const express = require("express");
const app = express();
const http = require("http");
const port = 5454;
const server = http.createServer(app);

let list = { people: [], places: [], things: [] };

const typeCheck = (req, res) => {
  const { type } = req.params;
  if (!Object.keys(list).includes(type))
    return res.send("Your type is invalid");
  next();
};
const homePage = (req, res) => {
  let header = <div>Homeeee</div>;
  res.send(header);
  
};
const returnTime = (req, res) => {
  const time = new Date.now();
  console.log(time);
  next();
};

const finalCall = (req, res) => {
  
};

app.get("/", returnTime, homePage;
app.get("/api");
app.get("/api/:type", typeCheck);

server.listen(port, () => console.log(`Server initialized on port ${port}`));
