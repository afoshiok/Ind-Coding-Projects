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
        <div id="card">
        </div>
    </section>
</template>

<script>
export default {
    name: 'test',
    props: [],
    data(){
        return{
            name: 'none'
        }
    },
    methods : {
        async getmovie(){
            const response = await fetch('https://ghibliapi.herokuapp.com/films')
            const results = await response.json()
            console.log(results)
            
            results.forEach(movie => {
                console.log(movie.title)
                const card = document.createElement('div')
                card.setAttribute('id','card')
                const h1 = document.createElement('h1')
                h1.textContent = movie.title
                card.appendChild(h1)
            })
        }
    },
}

</script>