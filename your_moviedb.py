#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pprint import pprint as pp
import sys
import json
import urllib

omdb_url = "http://www.omdbapi.com/"
imdb_url = "http://www.imdb.com/title/"
poster_placeholder = "http://entertainment.ie/movie_trailers/trailers/flash/posterPlaceholder.jpg" 
template = "template.html"
out_file = "topmovies.html"

def movies_to_query(lst):
  with open(lst) as f:
    return [li.strip() for li in f.readlines()]

def query_omdb(movie, year):
  """ get movie info (json) from omdb """
  # example URL: http://www.omdbapi.com/?t=city+of+god&y=&plot=short&r=json
  # you can also use omdb (pip install omdb)
  params = urllib.urlencode({ 't' : movie, 'y': year, 'plot' : "short", 'r': "json"})
  url = "%s?%s" % (omdb_url, params)
  f = urllib.urlopen(url)
  return json.loads(f.read())

def get_movie_data(lst):
  """ get movie data for all movie titles provided """
  movies = []
  for line in lst:
    if not "," in line and line.count(",") != 1:
      print >>sys.stderr, "ERR1: line without exactly one comma: %s" % line  
      continue
    (mov, year) = line.rsplit(',',1) # takes only the last comma!
    res = query_omdb(mov, year)
    if "Error" in res:
      print >>sys.stderr, "ERR2: cannot find movie: %s (year: %s)" % (mov, str(year))
      continue
    movies.append(res)
  return movies

def generate_movies_html(movies):
  """ generates the unordered list html for movies """
  out = [""]
  for i, m in enumerate(movies):
    if i % 3 == 0:
      out.append("<li class='clear'>")
    else:
      out.append("<li>")
    out.append("<h2>%s <small>(%s)</small></h2>" % (m["Title"], m["Year"]))
    out.append("<div class='genreWrapper'><p>%s" % m["Genre"])
    out.append("<br>Rated: %s</p></div>" % m["imdbRating"])
    poster = m["Poster"] if m["Poster"] != "N/A" else poster_placeholder
    out.append("<div class='poster'><img src='%s' alt='%s'></div>" % \
      (poster, m["Title"]))
    out.append("<div class='castWrapper'><h3>Cast</h3>")
    out.append("<p>Director: %s" % m["Director"])
    out.append("<br>Writer: %s" % m["Writer"])
    out.append("<br>Actors: %s</p></div>" % m["Actors"])
    out.append("<div class='plotWrapper'><h3>Plot</h3>")
    out.append("<p>%s</p></div>" % m["Plot"]) 
    out.append("<div class='specWrapper'>")
    out.append("<p>%s, %s votes, <a href='%s%s' target='_blank'>imdb</a></p></div>" % \
      (m["Runtime"], m["imdbVotes"], imdb_url, m["imdbID"]))
    out.append("</li>")
  return "\n\t\t".join(out).encode('ascii', 'ignore')

def create_html_page(movies):
  with open(template) as f:
    lines = f.readlines()
  ff = open(out_file, "w")
  for line in lines:
    if "LIST_MOVIES" in line:
      ff.write(line.replace("LIST_MOVIES", generate_movies_html(movies)))
    else:
      ff.write(line)
  ff.close()
  print "Done, %d processed, created static html movie page: %s" % (len(movies), out_file)
  

if __name__ == "__main__":
  # if no cli arg take default list, else what's given as first arg
  # movie list needs to be movie,year
  if len(sys.argv) < 2:
    movielist = "movielist.txt"
  else:
    movielist = sys.argv[1]
  if not os.path.isfile(movielist):
    sys.exit(movielist + " not found")
  movielist = movies_to_query(movielist)
  movies = get_movie_data(movielist)
  # pp(movies); sys.exit()
  create_html_page(movies)
