from math import ceil

def average_rating(movies):
    ''' Возвращает среднюю оценку по каталогу, 
        округленную до одного знака'''
    
    if not movies:
        return 0.0
    rating = sum(movie['rating'] for movie in movies)
    return round(rating/len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    '''Возвращает кортеж (самый старый фильм в годах, 
       самый новый фильм в годах, среднее), где среднее 
       округлено вверх до целого'''

    if movies:
        years = [movie['year'] for movie in movies]
    else:
        (None, None, None)

    return (min(years), max(years), round(sum(years)/len(movies)))
    

def duration_in_hours(minutes):
    ''' Переводит минуты в формат часы + минуты,
        используя целочисленное деление и остаток от деления'''

    if minutes >= 0:
        hours = minutes // 60
        minute = minutes % 60
    else:
        return print('Время не может быть отрицательным')
    
    return f"{hours} ч. {minute} мин."

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

avg = average_rating(movies)
print(f"Средний рейтинг {avg}")


func_2 = catalog_age_stats(movies)
print(f"Результат {func_2}")

print(duration_in_hours(-1))