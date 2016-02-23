#!/bin/bash
mymovies=my_movies_$(date +%s).txt
outfile=mymovies.html

echo "This is a test script for { Your movie site in just one minute }"
echo "See http://bobbelderbos.com/2016/02/movie-site-in-minute-omdb-api-python/ for more info"
echo 

echo
echo "1. creating textfile $mymovies with 10 movies in it"
printf "The Shawshank Redemption,1994\nThe Godfather,1972\nThe Godfather: Part II,1974\nThe Dark Knight,2008\nPulp Fiction,1994\nSchindler's List,1993\n12 Angry Men,1957\nThe Lord of the Rings: The Return of the King,2003\nThe Good, the Bad and the Ugly,1966" > $mymovies

echo
echo "2. importing required html template"
wget https://raw.githubusercontent.com/bbelderbos/own_movie_site/master/template.html

echo
echo "3. run the movie site creation script (via github)"
python <(curl -s https://raw.githubusercontent.com/bbelderbos/own_movie_site/master/your_moviedb.py) $mymovies

echo
echo "4. open the generated html site in default browser (mac, other OS, click on generateed $outfile)"
# say thanks
echo
command -v cowsay >/dev/null 2>&1 
if [ $? -eq 0 ];then 
  cowsay "Thanks $(id -un) for testing"; 
else
  echo "Thanks $(id -un) for testing"; 
fi
sleep 1

open $outfile
