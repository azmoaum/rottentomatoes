from optparse import OptionParser
import requests
import json
import config

# Container for a movie
class MovieParser:
    title_length = 0
    def __init__(self, movie):
        self.title = movie['title']
        self.year = movie['year']
        self.rating = movie['mpaa_rating']
        self.length = movie['runtime']
        self.critics_score = movie['ratings']['critics_score']
        self.audience_score = movie['ratings']['audience_score']
        self.cast = [str(member['name']) for member in movie['abridged_cast']]
        self.update_lengths()
    
    def update_lengths(self):
        length = len(self.title)
        if length > MovieParser.title_length:
            MovieParser.title_length = length

def print_rows(movies):
    print 'rows'
def print_table(movies):
    columns = '{0:{t_length}} {1} {2} {3} {4} {5}'.format('Title', 'Audience', 'Critics', 'Length', 'Rating', 'Year', t_length=MovieParser.title_length)
    print columns
    print '-'*len(columns)
    
    for movie in movies:
        print '{0:{t_length}} {1:<{a_length}} {2:<{c_length}} {3:<{l_length}} {4:<{r_length}} {5:<{y_length}}'.format(
            movie.title, movie.audience_score, movie.critics_score, movie.length, movie.rating, movie.year,
            t_length=MovieParser.title_length, a_length=len('Audience'), c_length=len('Critics'), l_length=len('Length'),
            r_length=len('Rating'), y_length=len('Year')
            )
            
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-s", "--source", dest="source")
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False)
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
    movies = [MovieParser(movie) for movie in json['movies']] 
    
    movies.sort(key=lambda x: x.audience_score, reverse=True)
    
    if opts.verbose:
        print_rows(movies)
    else:
        print_table(movies)