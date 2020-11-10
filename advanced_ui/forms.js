let loginform = document.querySelector("#login")
loginform.addEventListener("submit", evt => {
    evt.preventDefault()
    let results = [...evt.target.elements]
    .filter(param=>param.name)
    .map(p=>({name:p.name, value:p.value}))
    console.log(results)
    let bdy = document.querySelector("body")
    let d = document.createElement("div")
    bdy.append(d)
    for (i=0;i<=results.length;i++){
    d.append(`${results[i].name} : ${results[i].value}
    
    `)}
})


let date = document.createElement("input")
date.setAttribute("type", "date")
date.setAttribute("name", "date")
let email = document.createElement("input")
email.setAttribute("type", "email")
email.setAttribute("name", "email")
email.setAttribute("placeholder", "Email")
loginform.append(date, email)