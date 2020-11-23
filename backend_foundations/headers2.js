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
    <div class = "firstdiv">
        <p>
            You have committed a MASSIVE ERROR!!
        </p>

        <ul>
            <li>Mexican</li>
            <li>Italian</li>
            <li>Japanese</li>
        </ul>
    </div>
    <script>
        fetch(http://localhost:6565)
        .then(res=>res.json())
        .then(data=>{
            let listEl = document.querySelector("ul)
            data.forEach(item=>{
                let li = document.createElement("li")
                li.innerText = item.firstName+' '+item.lastName
                listEl.append(li)
            })})
    </script>
</body>
</html>
`;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.end(htmlFile);
});

const port = 7777;
server.listen(port, () => {
  console.log(`Server running on port: ${port}`);
});
