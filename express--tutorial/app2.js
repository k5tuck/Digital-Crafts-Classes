const express = require("express");
const app = express();
const http = require("http");
const fs = require("fs");
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

let people = require("./people.json");

app.get("/", (req, res) => res.send(servehHtml("Home")));

app.get("/api/people", (req, res) => {
  res.send(people);
});

app.get("/api/people/gender/:gender", (req, res) => {
  const { gender } = req.params;
  const personGender = people.filter((person) => person.gender == gender);
  res.send(personGender);
});

app.get("/api/people/email/:email", (req, res) => {
  const { email } = req.params;
  const personEmail = people.filter((person) => person.email == email);
  res.send(personEmail);
});

server.listen(port, () => {
  `Server initialized on Port: ${port}`;
});
