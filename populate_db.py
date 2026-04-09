from movies.models import Genre, Director, Movie, Review

# 1. Очищення бази перед наповненням
print("Очищення старої бази...")
Review.objects.all().delete()
Movie.objects.all().delete()
Director.objects.all().delete()
Genre.objects.all().delete()

# 2. Створення жанрів
print("Створення жанрів...")
genres = {
    'Drama': Genre.objects.create(name='Drama'),
    'Sci-Fi': Genre.objects.create(name='Sci-Fi'),
    'Thriller': Genre.objects.create(name='Thriller'),
    'Comedy': Genre.objects.create(name='Comedy'),
    'Crime': Genre.objects.create(name='Crime'),
    'Action': Genre.objects.create(name='Action'),
    'Horror': Genre.objects.create(name='Horror'),
}

# 3. Створення режисерів
print("Створення режисерів...")
directors = {
    'Nolan': Director.objects.create(first_name='Christopher', last_name='Nolan', birth_year=1970, country='UK'),
    'Tarantino': Director.objects.create(first_name='Quentin', last_name='Tarantino', birth_year=1963, country='USA'),
    'Villeneuve': Director.objects.create(first_name='Denis', last_name='Villeneuve', birth_year=1967,
                                          country='Canada'),
    'Scorsese': Director.objects.create(first_name='Martin', last_name='Scorsese', birth_year=1942, country='USA'),
    'Gerwig': Director.objects.create(first_name='Greta', last_name='Gerwig', birth_year=1983, country='USA'),
    'Fincher': Director.objects.create(first_name='David', last_name='Fincher', birth_year=1962, country='USA'),
}

# 4. Створення фільмів
print("Додавання 22 фільмів...")
movie_list = [
    # Нолан
    {'title': 'Inception', 'year': 2010, 'rating': 8.8, 'duration': 148, 'genre': genres['Sci-Fi'],
     'director': directors['Nolan']},
    {'title': 'Interstellar', 'year': 2014, 'rating': 8.6, 'duration': 169, 'genre': genres['Sci-Fi'],
     'director': directors['Nolan']},
    {'title': 'The Dark Knight', 'year': 2008, 'rating': 9.0, 'duration': 152, 'genre': genres['Action'],
     'director': directors['Nolan']},
    {'title': 'Oppenheimer', 'year': 2023, 'rating': 8.4, 'duration': 180, 'genre': genres['Drama'],
     'director': directors['Nolan']},

    # Тарантіно
    {'title': 'Pulp Fiction', 'year': 1994, 'rating': 8.9, 'duration': 154, 'genre': genres['Crime'],
     'director': directors['Tarantino']},
    {'title': 'Django Unchained', 'year': 2012, 'rating': 8.5, 'duration': 165, 'genre': genres['Drama'],
     'director': directors['Tarantino']},
    {'title': 'Kill Bill: Vol. 1', 'year': 2003, 'rating': 8.2, 'duration': 111, 'genre': genres['Action'],
     'director': directors['Tarantino']},

    # Вільнев
    {'title': 'Dune', 'year': 2021, 'rating': 8.0, 'duration': 155, 'genre': genres['Sci-Fi'],
     'director': directors['Villeneuve']},
    {'title': 'Arrival', 'year': 2016, 'rating': 7.9, 'duration': 116, 'genre': genres['Sci-Fi'],
     'director': directors['Villeneuve']},
    {'title': 'Blade Runner 2049', 'year': 2017, 'rating': 8.0, 'duration': 164, 'genre': genres['Sci-Fi'],
     'director': directors['Villeneuve']},
    {'title': 'Prisoners', 'year': 2013, 'rating': 8.1, 'duration': 153, 'genre': genres['Thriller'],
     'director': directors['Villeneuve']},

    # Скорсезе
    {'title': 'Shutter Island', 'year': 2010, 'rating': 8.2, 'duration': 138, 'genre': genres['Thriller'],
     'director': directors['Scorsese']},
    {'title': 'The Wolf of Wall Street', 'year': 2013, 'rating': 8.2, 'duration': 180, 'genre': genres['Comedy'],
     'director': directors['Scorsese']},
    {'title': 'The Departed', 'year': 2006, 'rating': 8.5, 'duration': 151, 'genre': genres['Crime'],
     'director': directors['Scorsese']},
    {'title': 'Killers of the Flower Moon', 'year': 2023, 'rating': 7.6, 'duration': 206, 'genre': genres['Crime'],
     'director': directors['Scorsese']},

    # Гервіг
    {'title': 'Barbie', 'year': 2023, 'rating': 6.9, 'duration': 114, 'genre': genres['Comedy'],
     'director': directors['Gerwig']},
    {'title': 'Lady Bird', 'year': 2017, 'rating': 7.4, 'duration': 94, 'genre': genres['Drama'],
     'director': directors['Gerwig']},
    {'title': 'Little Women', 'year': 2019, 'rating': 7.8, 'duration': 135, 'genre': genres['Drama'],
     'director': directors['Gerwig']},

    # Фінчер
    {'title': 'Fight Club', 'year': 1999, 'rating': 8.8, 'duration': 139, 'genre': genres['Drama'],
     'director': directors['Fincher']},
    {'title': 'Se7en', 'year': 1995, 'rating': 8.6, 'duration': 127, 'genre': genres['Crime'],
     'director': directors['Fincher']},
    {'title': 'Gone Girl', 'year': 2014, 'rating': 8.1, 'duration': 149, 'genre': genres['Thriller'],
     'director': directors['Fincher']},
    {'title': 'The Social Network', 'year': 2010, 'rating': 7.8, 'duration': 120, 'genre': genres['Drama'],
     'director': directors['Fincher']},
]

for m_data in movie_list:
    Movie.objects.create(**m_data)

# 5. Створення відгуків
print("Додавання відгуків...")
all_movies = Movie.objects.all()
if all_movies.exists():
    Review.objects.create(movie=all_movies.get(title='Inception'), text='Геніальний сюжет!', score=10)
    Review.objects.create(movie=all_movies.get(title='Oppenheimer'), text='Дуже сильна драма про науку.', score=9)
    Review.objects.create(movie=all_movies.get(title='Barbie'), text='Яскраво, але на один раз.', score=6)
    Review.objects.create(movie=all_movies.get(title='Fight Club'), text='Перше правило бійцівського клубу...',
                          score=10)
    Review.objects.create(movie=all_movies.get(title='Dune'), text='Неймовірний візуал.', score=9)
    Review.objects.create(movie=all_movies.get(title='Se7en'), text='Кінцівка просто шокує.', score=10)

print("Готово! База наповнена (22 фільми, 6 режисерів, 7 жанрів).")