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

//Interfaces 
interface UserInterface {
    readonly id: number, //readonly is pretty self explanitory, but that fuction can only be read.
    name: string,
    age ?: number  //"?:" means the property is optional. You won't get an error if you object doesn't include it.
}

const user1: UserInterface = {
    id: 1,
    name: 'Bob'
}

interface MathFunc {
    (x: number, y: number): number
}
const add: MathFunc = (x:number, y:number): number => x + y
const sub: MathFunc = (x:number, y:number): number => x - y
//Interface vs Type
type Point = number | string // Type works with Primitives and Unions
const p1: Point = 1

interface PersonInterface {
    id: number, //readonly is pretty self explanitory, but that fuction can only be read.
    name: string,
    register(): string
}

//Classes
class Person implements PersonInterface {
    private id: number //"Private" means that property can only be called within that class (See line 115 for error). You can also use "Protected" and "Public".
    name: string

    constructor(id: number, name: string){
        this.id = id
        this.name = name
    }

    register(){
        return `${this.name} is now registered`
    }
}

const brad = new Person(1, 'Brad Pitt')
const norm = new Person(2, 'Norm Fedder')

norm.id = 5


class Employee extends Person{
    position: string

    constructor(id: number, name: string, position: string){
        super(id,name)
        this.position = position
    }
}

const emp = new Employee(3, 'Shawn', 'Developer')

//Generics
function getArray<T>(items: T[]): T[]{  //T is a placeholder for the types.
    return new Array().concat(items)
}
let numArray = getArray<number>([1,2,3,4])
let strArray = getArray<string>(['Tom','Bill','Jack'])

numArray.push('Hello')


//use "tsc [name of ts file]" in the command line to compile the ts file to a js file. (Or just "tsc")
//use "tsc --watch [name of ts file]" to compile in watch mode, which doesn't create a js file.
//use "tsc init" to create a config file, which you can change many things about compilation. I changed the target from ES2016 to ES6 in this example.
