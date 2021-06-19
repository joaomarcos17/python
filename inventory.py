def my_films(e):
    return e['drama']

Dramas = [
    {'drama':'All want for love is you', 'year': 2019 },
    {'drama':'Meteor Garden', 'year': 2018 },
    {'drama': 'my Mr Mermaid', 'year': 2017 }
]

Dramas.sort(key=my_films)

print(Dramas)