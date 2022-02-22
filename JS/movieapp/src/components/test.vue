<script>
export default {
    name: 'test',
    props: []
}
getdata()//API console.log works now but it logs on load instead of on the click.
async function getdata(){
    const response = await fetch('https://ghibliapi.herokuapp.com/films')
    const data = await response.json()
    const obj = JSON.parse(this.data)
    obj.forEach(movie=> {
        console.log(movie.title)
    });
    console.log(data)
    } 
</script>

<template>
    <h1>MAIN VIEW TEST</h1>
    <section>
        <input type="text" 
        placeholder="Insert Movie Name"/>
        <button
        @click= "getdata()">Submit</button>
    </section>
</template>

