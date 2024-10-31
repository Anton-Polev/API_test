from pprint import pprint

import requests

url = "https://swapi.dev/api/people/4/"

l = []
s = set()

"""код который будет сохранять всех персонажей (имена), которые снимались в фильмах с Дарт Вейдером, в тестовый файл"""
def star_wars():
    """Список фильмов с Дарт Вейдером"""
    print("Список фильмов с Дарт Вейдером")
    dart = requests.get(url)
    dart_data = dart.json()
    dart_films = dart_data.get('films')
    assert dart.status_code == 200
    print(f"Статус код {dart.status_code}")
    print(dart_films)
    print('-' * 50)

    """Циклом по всем фильмам и внести урлы имен в множество"""
    print("Циклом по всем фильмам и внести урлы имен в множество")
    for i in dart_films:
        dart_films_r = requests.get(i)
        dart_films_r_data = dart_films_r.json()
        people = dart_films_r_data["characters"]
        s.update(people)
        assert dart_films_r.status_code == 200
        print(f"Статус код {dart_films_r.status_code} фильма {i}")
    pprint(s)
    print('-' * 50)

    """Циклом по множеству и извлечь урлы имен в список"""
    print("Циклом по множеству и извлечь урлы имен в список")
    for j in s:
        j_r = requests.get(j)
        j_data = j_r.json()
        l.append(j_data['name'])
        print(f"Статус код {j_r.status_code} имени {j}")
    pprint(l)
    print('-' * 50)

    """Циклом по списку и внести в файл"""
    print("Циклом по списку и внести в файл")
    with open('people.txt', 'a', encoding='utf-8') as file:
        for k in l:
            file.write(k + '\n')
    print('-' * 50)

    print('Готово')


star_wars()
