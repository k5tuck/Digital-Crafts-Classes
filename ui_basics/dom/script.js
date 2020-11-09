// getElements returns an HTML Collection [not iterable]
console.log("just testing stuff out")
let paragraphs = document.getElementsByTagName("p")
console.log(paragraphs)

let ideas = document.getElementsByClassName("concept")
console.log(ideas)

// for CSS
let heading = document.querySelector("h1")
console.log(heading)

//Only slecets one item id
let main = document.querySelector("#main-idea")
console.log(main)

//Selects class
let idea = document.querySelector(".child-idea")
console.log(idea)

// QuerySelector will always only select ONE item or null
// QuerySelectorAll will select all items of that 
// QuerySelector will make a Nodelist [iterable]

