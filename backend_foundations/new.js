const http = require("http");
const port = 5566;
const generateContent = require("./modules/generateHTML");
const makeHeading = require("./modules/makeheading");
const serveFile = require("./modules/serveFiles");

const server = http.createServer((req, res) => {
  res.writeHead(200);
  const url = new URL(req.headers.host + req.url);
  let page = url.searchParams.get("page");
  let count = url.searchParams.get("count");
  let additional = [];
  url.searchParams.forEach((value, name) => {
    additional.push(`<li>${name}:${value}</li>`);
  });
  let heading = makeHeading(page);
  let foo = "Yo are awesome Clint!";
  let wrapper = generateContent({
    page,
    heading,
    count,
    additional,
    foo,
  });
  res.write(wrapper);
  res.end();
});
server.listen(port);
