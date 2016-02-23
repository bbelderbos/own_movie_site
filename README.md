# Your own movie site in less than one minute with OMDb API and Python

* copy and paste top 250 movies from [imdb](http://www.imdb.com/chart/top) and put in file called inimdb-top-rated.txt file

    $ head  imdb-top-rated.txt 
      1. The Shawshank Redemption (1994)  9.2   
      
      2. The Godfather (1972)   9.2   
      
      3. The Godfather: Part II (1974)  9.0   
      
      4. The Dark Knight (2008)   8.9   
      
      5. Pulp Fiction (1994)  8.9   

* normalize the data to title,year:

    $ grep -v "^ *$" imdb-top-rated.txt |perl -pe 's/ *\d+\.\s+(.*)\s+.*\((\d+)\).*/\1,\2/g' > movielist.txt

    $ wc -l movielist.txt
        250 movielist.txt

    $ head movielist.txt
    The Shawshank Redemption,1994
    The Godfather,1972
    The Godfather: Part II,1974
    The Dark Knight,2008
    Pulp Fiction,1994
    Schindler's List,1993
    12 Angry Men,1957
    The Lord of the Rings: The Return of the King,2003
    The Good, the Bad and the Ugly,1966
    Fight Club,1999

* run the python script that queries [omdb](http://omdbapi.com/) for movie info returning a nice html page, 2% not found, but a movie html page in less than 1 minute :) 

    $ time python your_moviedb.py movielist.txt
    ERR2: cannot find movie: Old Boy (year: 2003)
    ERR2: cannot find movie: Érase una vez en América (year: 1984)
    ERR2: cannot find movie: M (year: 1931)
    ERR2: cannot find movie: Nader y Simin, una separación (year: 2011)
    ERR2: cannot find movie: Relatos salvajes (year: 2014)
    Done, 245 processed, created static html movie page: topmovies.html

    real 0m13.348s
    user 0m0.755s
    sys 0m0.420s

* see example output by opening topmovies.html output file in the browser or click [here](http://bobbelderbos.com/topmovies.html)
