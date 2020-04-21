from collections import namedtuple
Movie = namedtuple('Movie','title year score')

l = [
    Movie(title='A',year=1990,score=1),
    Movie(title='B',year=1991,score=1),
    Movie(title='C',year=1980,score=1),
    Movie(title='D',year=1970,score=1),
]

l.sort(reverse=True,key=lambda x: x.year)

for i in l:
    print(i)