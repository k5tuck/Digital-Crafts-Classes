// Create an array of vehicle objects.
//     each vehicle object needs to have keys of name, speed, passangers.
//     using map, create a list of names of the vehicles.

// Create an array of at least 6 todo items with each todo having keys, id, todo, status.
//     Limit the status to "complete","in-progress","todo"
//     Using map create a list of different status.
//     using map of those status, make a list of status objects that has keys status, and items.

// Exercise 1
// let vehicles = [
//     {
//         "name": "truck",
//         "speed": 65,
//         "passengers": 5
//     },
//     {
//         "name": "jeep",
//         "speed": 55,
//         "passengers": 4
//     },
//     {
//         "name": "motorcycle",
//         "speed": 120,
//         "passengers": 1
//     },
//     {
//         "name": "car",
//         "speed": 90,
//         "passengers": 5
//     }]
// let vehicleNames = vehicles.map((vehicle)=>vehicle.name)
// console.log(vehicleNames)

// Exercise 2
let todo_list = [
    {
        id: 1,
        todo: "laundry",
        status: "todo"
    },
    {
        id: 2,
        todo: "dishes",
        status: "todo"
    },
    {
        id: 3,
        todo: "bank run",
        status: "todo"
    },
    {
        id: 4,
        todo: "wash car",
        status: "todo"
    }]
todo_list.map((item)=>{
    let itemstatus = item.status
})