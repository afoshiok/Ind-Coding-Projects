require('dotenv').config({path: '.env'}); //Imports dotenv

const tmdb_key = process.env.TMDB_KEY
const query_runtime = `https://api.themoviedb.org/3/discover/movie?api_key=${tmdb_key}&language=en-US&sort_by=popularity.desc&vote_average.gte=8&with_runtime.lte=45` //Queried by average vote and runtime BUT runtime is not working...
const film_info = `https://api.themoviedb.org/3/movie/747059?api_key=${tmdb_key}&language=en-US`


fetch(query_runtime)
.then(response => response.json())
.then(data => {
    var result = data.results[0]
    console.log(result)
});

// fetch(film_info)
// .then(response => response.json())
// .then(data => {
//     var result = data
//     console.log(data)
// });

