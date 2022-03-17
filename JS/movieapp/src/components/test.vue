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
            require('dotenv').config();
            console.log(process.env)
            const film_api_key = process.env.film_api
            console.log(film_api_key)
            const response = await fetch(`https://api.themoviedb.org/3/trending/movie/week?api_key=${film_api_key}`)
            const data = await response.json()
            console.log(data)
            
        }
    },
}

</script>