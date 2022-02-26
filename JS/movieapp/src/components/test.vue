<template>
    <h1>MAIN VIEW TEST</h1>
    <section id = "#Runner">
        <input id="Input1"
        type="text" 
        placeholder="Doesn't do anything"/>
        <input id="Input2" type="text"
        placeholder="Neither does this one"/>
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
        }
    },
}

</script>