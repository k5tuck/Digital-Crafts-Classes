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
        console.log("You have committed a MASSIVE ERROR!!")
    </script>
</body>
</html>
`;

// Creating Server
const server = http.createServer((request, response) => {
  response.statusCode = 200;
  response.end(htmlFile);
});

// Assigning Port
const port = 5454;
server.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
