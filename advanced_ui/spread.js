// Exercise 1
// let letters = ["a", "b", "c", "d", "e"];
// let numbers = [1, 2, 3, 4, 5]

// let lettersfirst = [...letters, ...numbers]
// let numbersfirst = [...numbers, ...letters]
// console.log(lettersfirst)
// console.log(numbersfirst)

// Exercise 2
const cars = [
    {
        make:"Chevy",
        model:"Corvette",
        year:2019
    },
    {
        make:"Ford",
        model:"Mustang",
        year:2018
    },
    {
        make:"Tesla",
        model:"Model 3",
        year:2020
    },
    {
        make:"GMC",
        model:"h2",
        year:2010
    }
]
let additionalcars = [
    {make:"Nissan",
    model:"SkylineGTR",
    year:1998}, 

    {make:"Toyota",
    model:"Supra",
    year:1996}]

const new_cars = [...cars, ...additionalcars]

console.log(new_cars)

let oldcars = new_cars.filter(car => car.year < 2018)
console.log(oldcars)