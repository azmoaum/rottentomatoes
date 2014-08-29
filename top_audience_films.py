import requests
import json
from optparse import OptionParser
import config

class MovieParser:
    def __init__(self, movie):
        self.movie = movie
        self.parseMovie()
    
    def parseMovie(self):
        self.title = self.movie['title']
        self.year = self.movie['year']
        self.critics_score = self.movie['ratings']['critics_score']
        self.audience_score = self.movie['ratings']['audience_score']
    
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-s", "--source", dest="source")
    opts, args = parser.parse_args()
    
    if opts.source:
        if opts.source in config.API_URLS:
            url = config.API_URLS[opts.source]
        else:
            parser.error('Invalid source. Unable to continue')
    else:
        parser.error('--source required. Unable to continue')
    
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        response.raise_for_status()
        
    json = response.json()
    
    movies = json['movies']

    movies = [MovieParser(movie) for movie in movies] 
    
    for movie in movies:
        print movie.title, movie.audience_score
