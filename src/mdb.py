import sys
import tmdbsimple as tmdb

movie_name = sys.argv[1]

tmdb.API_KEY = 'TMDB_API_KEY'
search = tmdb.Search()
response = search.movie(query=movie_name)
for s in search.results:
    print( s['title'] + ' (' + s['release_date'].split("-")[0] + ') [480p]\\' + s['title'] + '.' + s['release_date'].split("-")[0] + '.480p.mv4' )


