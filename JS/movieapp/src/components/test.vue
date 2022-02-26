<template>
    <h1>MAIN VIEW TEST</h1>
    <section id = "#Runner">
        <input id="Input1"
        type="text" 
        placeholder="Insert Movie Name"/>
        <input id="Input2" type="text"
        placeholder="Enter something"/>
        <button
        v-on:click= "getmovie()">Submit</button>
        <div id="movie">{{name}}</div>
        <img v-bind:src="picture" :alt="poster">
    </section>
</template>

<script>

export default {
    name: 'test',
    props: [],
    data(){
        return{
            name: '', //title's unchanged state
            picture:'' //Poster's unchanged state
        }
    },
    methods : {
        async getmovie(){
            const response = await fetch('https://ghibliapi.herokuapp.com/films')
            const results = await response.json()
            console.log(results)
            this.name = results[0].title //changes title
            this.picture = results[0].image //changes name
            results.forEach(movie => {
                console.log(movie.title)
            })
        }
    },
}

</script>