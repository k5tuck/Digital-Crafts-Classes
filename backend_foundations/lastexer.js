const fs = require("fs");

let text = `Hello, my name is Kevin. I am officialy a beast at everything that I try because.. Jesus. 
some Text, and I have no clue what I'm dooooing. some Text, and I have no clue what I'm dooooing some Text, 
and I have no clue what I'm dooooing some Text, and I have no clue what I'm dooooing
some Text, and I have no clue what I'm dooooing some Text, and I have no clue what I'm dooooing some Text, 
and I have no clue what I'm dooooing`;

fs.writeFile("paragraph.txt", text, (err) => {
  if (err) throw err;
  console.log("File has been written");
});
