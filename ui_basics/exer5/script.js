let title = document.createElement("h1")
title.append("This is my New site")

let main = document.createElement("main")
let sec2 = document.createElement("section")
// let main = document.querySelector("main")
main.append(sec2)

let sectitle = document.createElement("h2")
sectitle.append("Section 2 Title")
sec2.append(sectitle)

let para = document.createElement("p")
para.append("Magna dolore irure ipsum adipisicing duis elit est nisi nulla fugiat nostrud quis.")
sec2.append(para)

let list = document.createElement("ul")
main.append(list)
for(i=0;i<5;i++){
    let item = document.createElement("li")
    item.append(`This is the ${i} item`)
    list.append(item)
}
let body = document.querySelector("body")
body.append(title)
body.append(main)