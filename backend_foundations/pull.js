const http = require("http");

let htmlFile = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <script>
        fetch("http://localhost:5555")
        .then(res=>res.json())
        .then(data=>{console.log(data)})
    </script>
</body>
</html>
`;

const server = http.createServer((req, res) => {
  res.setStatus = 200;
  let url = new URL(req.headers.host + req.url);

  let name = url.searchParams.get("name");
  let age = url.searchParams.get("age");

  let content = "";
  switch (name) {
    case "Joshua":
      content += `<h1>This is Joshua's Page!<h1>`;

      break;
    case "Alina":
      content += `<h1>This is Alina's Page!</h1>`;
      break;
    case "Matthew":
      content += `<h1>This is Matthew's Page!</h1>`;
      break;
    default:
      content += `<h1>This is Home</h1>`;
  }
  content += `<div>Age is ${age || 18}</div>`;

  res.write(content);
  res.end();
});

const port = 5000;
server.listen(port, () => {
  console.log(`server starting on port: ${port}`);
});
