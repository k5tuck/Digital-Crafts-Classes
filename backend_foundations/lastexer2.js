const fs = require("fs");

// let cars = [
//   {
//     name: "Jeep",
//     speed: "medium",
//     year: "2012",
//   },
//   {
//     name: "WRX",
//     speed: "fast",
//     year: "2008",
//   },
//   {
//     name: "Silverado",
//     speed: "medium",
//     year: "2020",
//   },
// ];
// fs.writeFile("cars.json", JSON.stringify(cars), (err) => {
//   if (err) throw err;
//   console.log("Cars json file created");
// });

// let cars = JSON.parse(fs.readFileSync("cars.json"));

// const addCar = (newCar) => {
//   cars.push(newCar);
//   fs.writeFile("cars.json", JSON.stringify(cars), (err) => {
//     if (err) throw err;
//     console.log("New car added");
//   });
// };

// addCar([
//   { name: "GTR", speed: "fast", year: "1998" },
//   { name: "Viper", speed: "fast", year: "2018" },
// ]);

// let ships = [
//   {
//     type: "Freighter",
//     speed: "medium",
//     cargo: "large",
//     payload: "low",
//   },
//   {
//     type: "Fighter",
//     speed: "fast",
//     cargo: "none",
//     payload: "medium",
//   },
//   {
//     type: "Bomber",
//     speed: "slow",
//     cargo: "none",
//     payload: "high",
//   },
// ];

// fs.writeFile("ships.json", JSON.stringify(ships), "utf8", (err) => {
//   if (err) throw err;
//   console.log("File created");
// });

let ships = JSON.parse(fs.readFileSync("ships.json"));

const addShip = (newShip) => {
  ships.push(newShip);
  fs.writeFile("ships.json", JSON.stringify(ships), "utf8", (err) => {
    if (err) throw err;
    console.log("New Ship added");
  });
};

addShip({
  type: "Zommer",
  speed: "fast",
  cargo: "Big Bertha",
  payload: "high",
});
