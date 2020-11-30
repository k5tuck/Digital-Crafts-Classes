const express = require("express");
const app = express();
const http = require("http");
const fs = require("fs");
const { send } = require("process");
const port = 5454;
const server = http.createServer(app);

let servehHtml = (req) =>
  `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${req}</title>
</head>
<body>
<h1>${req}</h1>
</body>
</html>
`;
const _404Content = `
    <!DOCTYPE html>
    <html> 
        <head> 
            <title>An Error you have found</title>
        </head>
        <body>
            <h1>404</h1>
            <blockquote>"An Error you have found" - Yoda
            </blockquote>
        </body>
    </html>
`;

const send404 = (req, res) => {
  res.status(404);
  res.send(_404Content);
};

const sendFavicon = (req, res) => {
  fs.readFile("/favicon.ico", (err, data) => {
    if (err) return res.send(err);
    res.send(data);
  });
};

app.get("/favicon.ico", sendFavicon);
app.get("/", (req, res) => res.send(servehHtml("Home")));
app.get("/home", (req, res) => res.send(servehHtml("Home")));
app.get("/about", (req, res) => res.send(servehHtml("About")));
app.get("*", send404);

server.listen(port, () => {
  `Server initialized on Port: ${port}`;
});
