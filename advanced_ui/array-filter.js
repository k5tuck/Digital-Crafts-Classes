let current_timestamp = new Date().getTime()
let past_timestamp = new Date(02/23/1979).getTime()

let todo_list = [
    {
        id: 1,
        todo: "laundry",
        status: "todo",
        deadline: past_timestamp,
    },
    {
        id: 2,
        todo: "dishes",
        status: "complete",
        deadline: past_timestamp,
    },
    {
        id: 3,
        todo: "bank run",
        status: "complete",
        deadline: current_timestamp,
    },
    {
        id: 4,
        todo: "wash car",
        status: "todo",
        deadline: current_timestamp
    }]
let completeTasks = todo_list.filter(item => item.status === "complete" ? true : false)
let soonest = todo_list.find(item=>item.status === "todo" ? true : false)

console.log(completeTasks)
console.log(soonest)

let pastdue = todo_list.filter(due => new Date (due.deadline).getTime() < Date.now())
console.log(pastdue)