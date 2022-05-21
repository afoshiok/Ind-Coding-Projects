//Learning with the "TypeScript Crash Course" video by Traversy Media

//Data Types
let id: number = 5
// id = '5'  /*You get an error because the variable id is given a number type.*/
let city: string = 'Houston, Texas'
let isGreatestCity: boolean = true
let o: any = 'Houston'

//Data Types for arrays
let ids: number[] = [1,2,3,4,5]
ids.push('Hi') //You will get an error, you cannot add 'Hi' to the ids array because it is a string.
let arr: any[] = ['hello',false,2]

//Tuple
let customer: [number,string,boolean] = [1,'John Smith',true]
//Tuple Array
let employee: [number, string][]
employee = [
    [1,'John'],
    [2,'Nick'],
    [3, 'Jerome'],
    [4, true] //ERROR bc array index 1 should be a string not a boolean
]

//Union
let uni_id: string | number
uni_id = 22 //You can use '22' and not get an error

//Enum
enum Direction1{
    Up = 1,
    Down,
    Left,
    Right,
}
console.log(Direction1.Up)

enum Direction2{
    Up = 'Up',
    Down = 'Down',
    Left = 'Left',
    Right = 'Right',
}

//Objects
type User = {
    id: number,
    name: string
}
const user: User = {
    id: 1,
    name: 'John'
}

//Type Assertion
let cid: any = 1
// let customerID = <number>cid
let customerId = cid as number

//Fuctions
function addNum(x: number,y: number): number {
    return x + y
}

function log(message: string | number): void{  //Void means you won't return anything
    console.log(message)
}


//use "tsc [name of ts file]" in the command line to compile the ts file to a js file. (Or just "tsc")
//use "tsc --watch [name of ts file]" to compile in watch mode, which doesn't create a js file.
//use "tsc init" to create a config file, which you can change many things about compilation. I changed the target from ES2016 to ES6 in this example.
