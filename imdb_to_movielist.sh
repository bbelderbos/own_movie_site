grep -v "^ *$" imdb-top-rated.txt |perl -pe 's/ *\d+\.\s+(.*)\s+.*\((\d+)\).*/\1,\2/g' > movielist.txt
