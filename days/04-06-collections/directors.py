#challenge013 - Highest Rated Movie Directors
from collections import defaultdict, namedtuple, Counter, deque, OrderedDict
import csv

movies_csv = './days/04-06-collections/movies.csv'

Movie = namedtuple('Movie','title year score')
def get_movies_by_director(data=movies_csv):
    """ Extracts all movies from CSV and stores them in a dictionary
        where keys are directors , and values is a list of movies (named tuples)"""
    directors = defaultdict(list)
    # Had an error (UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 4301: character maps to <undefined>)
    # Resolved by specifing the encoding
    with open(data, encoding='utf8') as f: 
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0','')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            
            m = Movie(title=movie,year=year,score=score)
            directors[director].append(m)
    return directors

def _calc_mean(movies):
    result = round(sum([movie.score for movie in movies])/len(movies),1)
    return result

def filter_directors(directors):
    filtered_directors=defaultdict(list)
    for director, movies in directors.items():
            if len(movies) >= 4:
                for movie in movies:
                    if movie.year >= 1960:
                        filtered_directors[director].append(movie)
    return filtered_directors

def get_average_scores(directors):
    filtered_directors = filter_directors(directors)
    cnt = Counter()
    for director, movies in filtered_directors.items():
        cnt[director] += _calc_mean(movies)
    return cnt

directors = get_movies_by_director()

required_directors = filter_directors(directors)

dir_average_score = get_average_scores(required_directors)

top20 = enumerate(dir_average_score.most_common(20),start=1)

#Display results
for enum,(director,score) in top20:
    print (f"{enum:2}. {director:83} {score:3}")
    print('-'*30)
    directors[director].sort(reverse=True,key=lambda k: k.year)
    for movie in directors[director]:
        print(f"{movie.year:4}] {movie.title:80}  {movie.score:3}")
    print(' ')
