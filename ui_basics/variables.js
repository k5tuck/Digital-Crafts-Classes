// // Exercise 1
// let a = 1;
// let b= 2;
// let c = 3;
// console.log(a,b,c)

// //Exercise 2
// const randomNum = 29;
// console.log(randomNum)

// //Exercise 3
// let name="Kevin", age = "thirty", day = "Monday";
// console.log(name, age, day)

// //Exercise 4
// let boo = 23;
// let boo4;
// const mscvo = 9;
// const und = undefined;
// console.log(boo, boo4, mscvo, und)

// //Exercise 5
// let value = 0;

// if(value===10){
//     console.log("value is not 20")
// } 
// else if(value === 20){
//     console.log("value is 20")
// }
// else{
//     console.log("value is unknown")
// }

// //Exercise 6
// let firstNumber = 3;
// let secondNumber = 4;
// let result = undefined;
// firstNumber > secondNumber ? result = "result is higher":result = "result is lower";
// console.log(result)

// //Exercise 7
// const temp = 73;
// let color;

// switch(true){
//     case (temp < 0):
//         color = "#4768d7"
//         break;
//     case (temp < 30):
//         color = "#112e91"
//         break;
 
//     case (temp < 50):
//         color = "#491191"
//         break;

//     case (temp < 75):
//         color = "#0ca611"
//         break;
//         console.log(color)
//     case (temp < 80):
//         color = "#0ba1a7"
//         break;
//         console.log(color)
//     case (temp < 90):
//         color = "#07b757"
//         break;
//         console.log(color)
//     case (temp > 90):
//         color = "#860000"
//         break;
//     default:
//         color = "#00023f"
// }
// console.log(color)

// // Exercise 8
// let i = 0;
// let sum = 0;
// while (i <= 10){
//     sum+=i;
//     i++
// }
// console.log(sum);

// // Exercise 9
// for(let j = 10; j < 100; j+=10){
//     console.log(j);
// }

// Homework

// Exercise 10
let idiv = 6;
for (let n = 300; n/=idiv; idiv--){
    console.log(n);
    if (idiv === 4){
        break;
    }
}

// Exercise 11
let sum = 0;
for (let numi = 0; sum += numi; numi++){
    if (numi % 2 == 0){
        continue;
    }
    else if (numi % 3 == 0){
        continue;
    }
    else{
        console.log("Printing next number")
    }
}
console.log(sum)

// Exercise 12
function addNumbers(a, b, c){
    let result;
    result = a+b+c;
    return result;
}

// Exercise 13
function example(funcexample){
    funcexample()
}

example(function anon() {
    console.log("A new world")
})

