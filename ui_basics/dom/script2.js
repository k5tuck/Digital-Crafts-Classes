let main = document.querySelector("body")

let divider = document.createElement("div")
let order = document.createElement("ol")
main.append(divider, order);


for(let i=0; i<5;i++){
    let item = document.createElement("li")
    item.append("Kevin's cooking Item")
    order.append(item)
}

//Basically jquery
const $ = function (selector) {
    let r = document.querySelectorAll(selector)
    if(r.length < 2) return r[0];
    return r
}
 