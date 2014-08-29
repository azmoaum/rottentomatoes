import requests
import json
from optparse import OptionParser

API_KEY = 'a9qbanswywry5hubn5tqmw3t'

class MovieParser:
    def __init__(self, movie):
        self.movie = movie
        self.parseMovie()
    
    def parseMovie(self):
        self.title = self.movie['title']
        self.year = self.movie['year']
        self.critics_score = self.movie['ratings']['critics_score']
        self.audience_score = self.movie['ratings']['audience_score']

def retreive_json(source):
    url = {
        'BoxOffice': 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/box_office.json?apikey=%s' % API_KEY,
        'Theaters': 'http://api.rottentomatoes.com/api/public/v1.0/lists/dvds/new_releases.json?apikey=%s' % API_KEY,
        'Opening': 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/opening.json?apikey=%s' % API_KEY,
        'Upcoming': 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/upcoming.json?apikey=%s' % API_KEY,
        'TopRentals': 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/opening.json?apikey=%s' % API_KEY,
        'CurrentDVD': 'http://api.rottentomatoes.com/api/public/v1.0/lists/dvds/current_releases.json?apikey=%s' % API_KEY,
        'NewDVD': 'http://api.rottentomatoes.com/api/public/v1.0/lists/dvds/new_releases.json?apikey=%s' % API_KEY,
        'UpcomingDVD': 'http://api.rottentomatoes.com/api/public/v1.0/lists/dvds/upcoming.json?apikey=%s' % API_KEY
    }[source]
    response = requests.get(url)
    return response.json()
        
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-s", "--source", dest="source")
    opts, args = parser.parse_args()

    json = retreive_json(opts.source)
    movies = json['movies']

    for movie in movies:
        print movie['ratings']['audience_score']

    
