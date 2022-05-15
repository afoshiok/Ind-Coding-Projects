require('dotenv').config({path: '.env'}); //Imports dotenv

const tmdb_key = process.env.TMDB_KEY
const query_runtime = `https://api.themoviedb.org/3/discover/movie?api_key=${tmdb_key}&language=en-US&sort_by=popularity.desc&vote_average.gte=8&with_runtime.lte=45` //Queried by average vote and runtime [Runtime works now]
const film_info = `https://api.themoviedb.org/3/movie/831827?api_key=${tmdb_key}&language=en-US`



function get_movies() {
    fetch(query_runtime)
    .then(response => response.json())
    .then(data => {
    var result = data.results[0]
    console.log(result)
})    
}

let runtime_filter = 400  //this will be later replaced with the flight duration

fetch(film_info)
.then(response => response.json())
.then(data => {
    var result = data
    console.log(result)
    runtime_filter = runtime_filter - result.runtime //This subracts the movie runtime from the runtime filter. This will be done over and over from the loop
    console.log(runtime_filter)
});



// while (runtime_filter > 10 ){
//     get_movies()
// }

