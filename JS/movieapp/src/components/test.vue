<template>
    <h1>MAIN VIEW TEST</h1>
    <section id = "#Runner">
        <input id="Orig"
        type="text" 
        placeholder="From"/>
        <input id="Dest" type="text"
        placeholder="To"/>
        <button
        v-on:click= "getmovie()">Submit</button>
        <div id="movie">{{name}}</div>
        <h1>{{org_title}}</h1>
        <img v-bind:src="picture" :alt="picture">
    </section>
</template>

<script>
require('dotenv').config()
console.log(process.env)

export default {
    name: 'test',
    props: [],
    data(){
        return{
            name: '', //title's unchanged state
            picture:'', //Poster's unchanged state
            org_title: ''
        }
    },
    methods : {
        async getmovie(){
            const response = await fetch('https://ghibliapi.herokuapp.com/films')
            const results = await response.json()
            console.log(results)
            var pos = Math.floor(Math.random()*results.length) //Gets random array position
            this.name = results[pos].title //changes title
            this.picture = results[pos].image //changes name
            this.org_title = results[pos].original_title
            results.forEach(movie => {
                console.log(movie.title)
            })
        },
        async getdistance(){
            var from_value = from_value
            document.getElementById('Orig').value = from_value
            var to_value = to_value
            document.getElementById('Dest').value = to_value
            //const dist_response = await fetch(`https://api.distancematrix.ai/maps/api/distancematrix/json?origins=${from_value}&destinations=${to_value}=<your_access_token>`) //Distance Matrix API Set to expire on 3/18/21 currently looking for a new one
        } //This function gets the distance between 2 points.
    },
}

</script>