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
        return "Входное значение должно быть строкой"
    words = title.split()
    string = ""
    for word in words:
        string += word[0].upper() + word[1:] + " "
    return print(string)

def make_slug(title):
    '''Превращает номрализованное название в "слаг" 
        вида the-quiet-algorithm'''
    if not isinstance(title, str):
        return "Входное значение должно быть строкой"
    words = title.lower().split()
    string = ""
    for word in words:
        string += word + "-"
    string = string[:-1]
    return print(string) 

def format_report_line(movie):
    '''Возвращает единую строку с описанием фильма
    "The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi '''
    title = movie['title']
    year = movie['year']
    rating = movie['rating']
    time = duration_in_hours(movie['duration_min'])
    genres = ', '.join(sorted(list(movie['genres'])))
    result = f'"{title}" ({year}) - {rating}/10, {time}, жанры: {genres}'
    return print(result)

def titles_sorted_by_rating(movies):
    '''Возвращает список названий фильмов, отсортированных по убыванию рейтинга '''
    sort_movies = sorted(movies, key = lambda x: x['rating'], reverse = True)
    print('sort_movies   :',sort_movies)
    result = [movie['title'] for movie in sort_movies]
    return result  

def top_n_by_rating(movies, n=3):
    '''Возвращает список из n кортежей (title, rating), топ по рейтингу'''
    sort_movies = sorted(movies, key = lambda x: x['rating'], reverse=True)
    top_movies = sort_movies[:n]
    result = [((movie['title']),movie['rating']) for movie in top_movies]
    
    return result

def count_by_genre(movies):
    ''' Возвращает словарь {жанр: количество фильмов}'''
    #Найдем уникальные навания жанров в movies
    unic_genres = set()
    for movie in movies:
        for genre in movie.get('genres', []):
            unic_genres.add(genre)
    #Для каждого уникального названия жанра найдем соответствие в movies и запишем в словарь
    result = dict()
    for gen in unic_genres:
        count = 0
        for movie in movies:
            for genre in movie.get('genres',[]):
                if gen == genre: 
                    count += 1
                    result[gen] = count            
    return result

def actor_filmography(movies):
    ''' Возвращает словарь {актер: [список названий фильмов]}'''
    unic_actor = set()
    for movie in movies:
        for actor in movie.get('actors', []):
            unic_actor.add(actor)

    result = dict()
    for act in unic_actor:
        for movie in movies:
            for actor in movie.get('actors',[]):
                if act == actor: 
                    result.setdefault(act,[]).append(movie.get('title'))
    return result    

def all_genres(movies):
    '''Возвращает множество всех уникальных жанров каталога'''
    unic_ganres = set()
    for movie in movies:
        unic_ganres |= set(movie.get('genres',[]))
    return unic_ganres

def common_actors(movie1, movie2):
    '''Возвращает множество актеров снимавшихся в обоих фильмах'''
    actors1 = set()
    actors2 = set()
    for movie in movies:
        if movie.get('title') == movie1['title']:
            for actor in movie.get('actors', []):
                actors1.add(actor)
        elif movie.get('title', []) == movie2['title']:
            for actor in movie.get('actors', []):
                actors2.add(actor)
    
    return actors1 & actors2

def genres_only_in_one(movies_a, movies_b):
    '''Возвращает жанры встречающиеся в movies_a и не встречающиеся в movies_b'''
    #genres_a = set(movies_a.get('genres',[]))
    #genres_b = set(movies_b.get('genres',[]))
    genres_a = set()
    genres_b = set()
    for movie in movies_a:
        genres_a |= set(movie.get('genres',[]))
    for movie in movies_b:
        genres_b |= set(movie.get('genres',[]))
        
    result = genres_a - genres_b
    return result

def iter_high_rated(movies, min_rating=8.0):
    ''' Отдает фильмы с рейтингом не ниже min_rating'''
    for movie in movies:
        if movie['rating'] >= min_rating:
            yield movie


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

#print(f"Количество фильмов длиннее 120 минут:  {count_long_movies(movies, threshold=120)}")

#d_films = {movie['title']: movie['rating'] for movie in movies if movie['rating'] > average_rating(movies)}

print(genres_only_in_one(movies[5:6], movies[:5]))

for movie in iter_high_rated(movies):
    format_report_line(movie)