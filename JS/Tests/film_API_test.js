require('dotenv').config({path: '.env'}); //Imports dotenv

const tmdb_key = process.env.TMDB_KEY
const query_runtime = `https://api.themoviedb.org/3/discover/movie?api_key=${tmdb_key}&language=en-US&sort_by=popularity.desc&vote_average.gte=8&with_runtime.lte=45` //Queried by average vote and runtime [Runtime works now]


function get_movie_id(film_info){
    fetch(film_info)
    .then(response => response.json())
    .then(data => {
    var result = data
    // console.log(result)
    runtime_filter = runtime_filter - result.runtime //This subracts the movie runtime from the runtime filter. This will be done over and over from the loop
    console.log(runtime_filter)
});
}


function get_movies() {
    fetch(query_runtime)
    .then(response => response.json())
    .then(data => {
    var result = data.results[Math.floor(Math.random() * 5)]
    let movie_id = result.id
    console.log(result)
    console.log('film id is:',movie_id)
    const film_info = `https://api.themoviedb.org/3/movie/${movie_id}?api_key=${tmdb_key}&language=en-US`
    get_movie_id(film_info)
})    
}

get_movies()


let runtime_filter = 400  //this will be later replaced with the flight duration






// while (runtime_filter > 10 ){
//     get_movies()
// }

