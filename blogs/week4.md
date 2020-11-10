# Javascript Basics

## DOM

The `document.getElementsbyTags` lets you grab specific elements and makes an HTML collection out of your requested tag. 'non-iterable'

`document.querySelector()` is what is mainly used now and allows you to select one "CSS" element, class, or id at a time. `document.querySelectorAll()` lets you choose multiple of these and makes a Nodelist out of them. 'iterable'

`document.createElement` allows you to create an HTML element. The `.append` function will add whatever elements to another element that you select. Example:

```Javascript
let main = document.querySelector("body")
let divider = document.createElement("div")
let order = document.createElement("ol")
main.append(divider, order);
for(let i=0; i<5;i++){
    let item = document.createElement("li")
    item.append("Kevin's cooking Item")
    order.append(item)
}
```

### Attributes

Attributes can be changed for elements through the dot notation.

```Javascript
let main = document.querySelector("body")
let img = document.createElement("img")
img.src = "https://cdn.hiconsumption.com/wp-content/uploads/2019/04/2020-Nissan-GT-R-Nismo-Edition-0-Hero-1087x725.jpg"
img.alt = "2020 Nissan GT-R"
main.append(img)
```

### DOM Style

Changing Style in the DOM
The below code will change the whole style object

```Javascript
let header = document.querySelector("h1")
header.style = "border-bottom: 1px solid; text-align:center"
```

The below code will change a specific attribute in style. If CSS element is hyphened, use Camel case

```Javascript
header.style.color = "lightgreen"
header.style.borderBottom = "5px thick double lightblue"
```

### Classes

You can add classes to an element using the dot notation classList method.

```Javascript
let footer = dcoument.querySelector("footer")
footer.classList.add("randomName", "btn")
footer.classList.remove("btn")
```

```Javascript
let myInterval = setInterval(function(){
      myButton.classList.toggle("hidden")
  }, //timeinterval)
)

//Replace Class
let footer = document.querySelector("footer");
footer.classList.replace("highlighted","primary")

let res = footer.classList.contains("foo-bar")
console.log(res)
```
