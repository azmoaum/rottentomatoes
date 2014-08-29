API_KEY = 'a9qbanswywry5hubn5tqmw3t'
API_BASE = 'http://api.rottentomatoes.com/api/public/v1.0'

API_URLS = {'BoxOffice': '%s/lists/movies/box_office.json?apikey=%s' % (API_BASE, API_KEY),
            'Theaters': '%s/lists/dvds/new_releases.json?apikey=%s' % (API_BASE, API_KEY),
            'Opening': '%s/lists/movies/opening.json?apikey=%s' % (API_BASE, API_KEY),
            'Upcoming': '%s/lists/movies/upcoming.json?apikey=%s' % (API_BASE, API_KEY),
            'TopRentals': '%s/lists/movies/opening.json?apikey=%s' % (API_BASE, API_KEY),
            'CurrentDVD': '%s/lists/dvds/current_releases.json?apikey=%s' % (API_BASE, API_KEY),
            'NewDVD': '%s/lists/dvds/new_releases.json?apikey=%s' % (API_BASE, API_KEY),
            'UpcomingDVD': '%s/lists/dvds/upcoming.json?apikey=%s' % (API_BASE, API_KEY)
           }