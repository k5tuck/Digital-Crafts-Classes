const { write } = require("fs");
const http = require("http");

const ppl = [
  { firstName: "John", lastName: "Smith", email: "John.Smith@gmail.com" },
  { firstName: "Kevin", lastName: "Tucker", email: "Kevin.Tucker@new.com" },
  {
    firstName: "Susie",
    lastName: "Barker",
    email: "sb65@getComputedStyle.com",
  },
  { firstName: "Joe", lastName: "McBarter", email: "JBarter97@mail.com" },
  { firstName: "Yulo", lastName: "Yun", email: "YY79@yahoo.com" },
];

const server = http.createServer((req, res) => {
  res.writeHead(200, {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
  });
  res.write(JSON.stringify(ppl));
  res.end();
});

const port = 6565;
server.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
