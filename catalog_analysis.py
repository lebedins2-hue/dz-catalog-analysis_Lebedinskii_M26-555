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

    return (current_year - min(years), current_year - max(years), 
            current_year - ceil(sum(years)/len(movies)))
    

def duration_in_hours(minutes):
    ''' Переводит минуты в формат часы + минуты,
        используя целочисленное деление и остаток от деления'''
    if minutes >= 0:
        hours = minutes // 60
        minute = minutes % 60
    else:
        return print('Время не может быть отрицательным')
    
    return f"{hours} ч. {minute} мин."

def rating_tier(rating):
    ''' по оценке возвращает категорию: "шедевр" (≥9),
      "хорошо" (7–8.9), "средне" (5–6.9), "слабо" (<5).'''
    if not isinstance(rating, (int, float)):
        return "Рейтинг фильма должен быть числом"
    if rating >= 9:
        result = 'шедевр'
    elif rating >= 7:
        result = 'хорошо'
    elif rating >= 5:
        result = 'средне'
    else:
        result = 'слабо'
    return result

def decade_label(year):
    '''Возвращает через оператор match возвращает метку "новые" 
    (после 2020), "недавние" (2015–2020) или "старые" (раньше 2015).'''
    if not isinstance(year, int):
        return 'Год фильма должен быть чилсом'
    match year:
        case x if x >= 2020:
            return 'Новые'    
        case x if 2015 <= x <2020:
            return 'недавние'
        case x if 0 < x < 2015:
            return 'старые' 
        case x if x < 0:
            return 'год фильма не может быть отрицательным'
        
def count_long_movies(movies, threshold=120):
    '''Возвращает количество фильмов длиннее threshold минут'''
    count = 0
    for movie in movies:
        if movie['duration_min'] > threshold:
            count += 1
    return count

def normalize_title(title):
    '''Приводит строку к формату Title Case'''
    if not isinstance(title, str):
        return "Введите пожалуйста строку"
    words = title.split()
    string = ""
    for word in words:
        string += word[0][0].upper() + words[0][1:] + " "
        word = title.split()
    return string
    
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

print("Фильмы не относящиеся к жанру comedy")
for movie in movies:
    if "comedy" in movie.get('genres', []): continue
    print(movie['title'])

counter = 0    
while counter < len(movies):
    if rating_tier(movies[counter].get('rating', [])) == 'шедевр':
        print('Первый по порядку в списке фильм с рейтингом выше 9.0:  ',
              movies[counter].get('title', 'Без названия'))
        break
    counter += 1
else:
    print('Шедевров не найдено')

print(f"Количество фильмов длиннее 120 минут:  {count_long_movies(movies, threshold=120)}")

title = 'sdfsdf dsfsdfsdf sdf sdf'
print(normalize_title(title))