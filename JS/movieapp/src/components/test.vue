<template>
    <h1>MAIN VIEW TEST</h1>
    <section>
        <input type="text" 
        placeholder="Insert Movie Name"
        :value="movie"/>
        <button
        v-on:click= getdata()>Submit</button>
    </section>
</template>

<script>
export default {
    name: 'test',
    props: []
}
getdata()
async function getdata(){
    const response = await fetch('https://ghibliapi.herokuapp.com/films')
    const data = await response.json()
    } //Trying to test use of APIs with the Ghibli API but it isn't working...

</script>