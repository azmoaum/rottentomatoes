import getopt
import sys
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
        self.cast = ', '.join(self.cast)
        self.update_length()
    
    def update_length(self):
        length = len(self.title)
        if length > MovieParser.title_length:
            MovieParser.title_length = length

def parse_opts(argv):
    opts, args = getopt.getopt(argv, 's:hv', ['source=', 'help', 'verbose'])
    
    source = None
    verbose = False
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print_usage()
        elif opt in ('-s', '--source'):
            source = arg
        elif opt in ('-v', '--verbose'):
            verbose = True

    if source not in config.API_URLS:
        print_usage()
    
    return source, verbose

def print_usage():
   print 'Usage: top_audience_films.py [-s[--source] <BoxOffice|Theatres|Opening|Upcoming|TopRentals|CurrentDVD|NewDVD|UpcomingDVD>]\n'
   print 'Optional Arguments:'
   print '[-v[--verbose]]'
   print '[-h[--help]]'
   sys.exit(2) 
    
def print_rows(movies):
    for movie in movies:
        print 'Title: {0}\nAudience Score: {1}\nCritics Score: {2}\nLength: {3}\nRating: {4}\nYear: {5}\nCast: {6}'.format(
            movie.title, movie.audience_score, movie.critics_score, movie.length, movie.rating, movie.year, movie.cast)
        print
        
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
    (source, verbose) = parse_opts(sys.argv[1:])
    
    url = config.API_URLS[source]
    
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        response.raise_for_status()
    
    json = response.json()
    movies = [MovieParser(movie) for movie in json['movies']] 
    
    movies.sort(key=lambda x: x.audience_score, reverse=True)
    
    if verbose:
        print_rows(movies)
    else:
        print_table(movies)
        
    sys.exit(0)