//Exercise 1
for (let i = 0; i < 100; i++) {
  console.log(i);
}

//Exercise 2
function cowSays(input) {
  console.log(`The cow says "${input}"`);
}
cowSays("Mooooo");
cowSays("I'm reeeady to eat");
cowSays("I'm done");

//Exercise 3
let people = [
  { name: "batman", powers: "none" },
  { name: "iron man", power: "rich" },
  { name: "The Hulk", powers: "being green" },
  { name: "Superman", powers: "Being an Alien" },
];

//------- Wrong ---------
const pplName = new Map(people);
console.log(pplName);
// -----------------------
