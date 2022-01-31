import csv
import urllib.request #previously in python 2 we had urllib only but from Python3 urllib has been divided into many modules

movie_data='https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movie_csv='movie.csv'
urllib.request.urlretrieve(movie_data,movie_csv) #urlretrieve brings the data from remote place lets say a website and loads it into a local host

with open(movie_csv,'r') as csv_file:    
    csv_reader=csv.DictReader(csv_file) #this method DictReader() makes the file in dictionary format ("key":"value") format
    for line in csv_reader:
            print('Directory of the movie ',line['movie_title'], '----->', line['director_name'] )
 