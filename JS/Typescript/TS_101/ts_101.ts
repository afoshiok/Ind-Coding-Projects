//Learning with the "TypeScript Crash Course" video by Traversy Media
let id: number = 5
id = '5' //You get an error because the variable id is given a number type.

//use "tsc [name of ts file]" in the command line to compile the ts file to a js file.
//use "tsc --watch [name of ts file]" to compile in watch mode, which doesn't create a js file.
//use "tsc init" to create a config file, which you can change many things about compilation. I changed the target from ES2016 to ES6 in this example.
