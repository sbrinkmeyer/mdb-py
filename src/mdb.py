#!/usr/bin/env python3

import sys
import os
import tmdbsimple as tmdb

movie_name = sys.argv[1]

TMDB_API_KEY = os.getenv('TMDB_API_KEY')

tmdb.API_KEY = TMDB_API_KEY

while movie_name != '':
  search = tmdb.Search()
  response = search.movie(query=movie_name)
  for s in search.results:
      print( s['title'] + ' (' + s['release_date'].split("-")[0] + ') [480p]\\' + s['title'] + '.' + s['release_date'].split("-")[0] + '.480p.mv4' )
  print(' == Another search?')
  movie_name = input()

