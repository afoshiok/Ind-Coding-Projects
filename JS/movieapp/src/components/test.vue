<template>
    <h1>MAIN VIEW TEST</h1>
    <section id = "#Runner">
        <input id="Input1"
        type="text" 
        placeholder="Insert Movie Name"/>
        <input id="Input2" type="text"
        placeholder="Enter something"/>
        <button
        @click= "getmovie">Submit</button>
        <p>{{name}}</p>
    </section>
</template>

<script>
export default {
    name: 'test',
    props: [],
    data(){
        return{
            name: "movie"
        }
    },
    methods : {
        getmovie : getmovie()
    },
}
getmovie()//I think I got this to work but the library im in is blocking the API call.
async function getmovie(){
    const response = await fetch('https://ghibliapi.herokuapp.com/films')
    const data = await response.json()
    const obj = JSON.parse(this.data)
    obj.forEach(movie=> {
        console.log(movie.title)
    });
    console.log(data)
    } 
</script>