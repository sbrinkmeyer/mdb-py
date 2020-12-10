# mdp-py

so this is a small python to query the tmdb with your own api key to do a simple search for a title and it'll send back all the things it finds like this
blah (year) [480p]\blah.year.480p.m4v
did this to save me look ups and stuff and theres probably something out there already.

yes i could just have the docker container run the python in a loop looking for input ... maybe thats next.

theres a helper script as well called
  docker_run.sh
trying to separate the api key in to some sort of secrets storage without going too crazy.
