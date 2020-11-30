const http = require("http");
const fs = require("fs");
const port = 5454;

let content = `
<h1>This is the Title</h1>
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
  <li>Item 4</li>
</ul>
`;
let html = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New</title>
    <link rel="stylesheet" href="main.css">
</head>
<body>
  ${content}
</body>
</html>
`;

const css = (res) => {
  fs.readFile("main.css", (err, data) => {
    if (err) {
      res.writeHead(404);
      res.end(console.log("ERROR!!"));
    }
    res.writeHead(200, {
      "Content-Type": "text/css",
    });
    res.end(data);
  });
};

const favicon = (res) => {
  fs.readFile("favicon.io", (err, data) => {
    if (err) {
      res.writeHead(404);
      res.end(console.log("ERROR!!"));
    }
    res.writeHead(200);
    res.end(data);
  });
};

const makeHeading = (page) => {
  let heading;
  switch (page) {
    case "about":
      heading = `<h1>This is about!</h1>`;
      break;
    case "contact":
      heading = `<h1>This is contact</h1>`;
      break;
    case "foo":
      heading = "<h1>I Pitty THE foo</h1>";
      break;
    default:
      heading = `<h1>This is Home</h1>`;
  }
  return heading;
};

const server = http.createServer((req, res) => {
  if (req.url === "./favicon.ico") {
    return favicon();
  }
  if (req.url === "./main.css") {
    return css();
  }

  // const url = new URL(req.headers.host + req.url);
  // const page = url.serveParams.get("page");
  //   const new = url.serveParams.get("new");

  res.writeHead(200, {
    "Access-Control-Allow-Content": "*",
  });

  res.write(html);
  res.end();
});
server.listen(port, () => {
  console.log(`Server initiated on Port: ${port}`);
});
