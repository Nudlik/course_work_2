import re
import requests
from bs4 import BeautifulSoup
import config
import json
import random
import models
import os


def get_html(user_word: str = 'Набор', headers: dict = config.HEADERS) -> str:
    """Получаем html страницу по заданному слову от пользователя"""
    url = r'https://wordhelp.ru/comb/{}'.format(user_word)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text


def get_words(path_to_html: str) -> list:
    """Получаем слова из html файла"""

    # парсим html страницу
    html = read_html(path_to_html)
    soup = BeautifulSoup(html, 'html.parser')
    res = soup.find_all(class_='list-inline results')

    # выбираем слова больше 2 букв
    words_lst = []
    for words in res:
        words = words.text.strip().split()
        for word in words:
            if len(word) > 2 and word.isalpha() and word != 'стоп':
                words_lst.append(word)
    return words_lst


def html_to_file(file_name: str, html: str) -> None:
    """Записываем html в фаил"""
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(str(html))


def read_html(file_name: str) -> str:
    """Читает html файл"""
    if not os.path.exists(file_name):
        raise models.HthmlFileNotFound(f'Файл {file_name} не найден')
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()


def load_random_word(path_json: str) -> dict:
    """Вытаскиваем рандомно словарь из json"""
    if not os.path.exists(path_json):
        raise models.JsonFileNotFound(f'Файл {path_json} не найден')
    with open(path_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return random.choice(data)


def online_game(path: str, headers: dict) -> tuple:
    """Режим онлайн"""
    print('Напишите слово из букв которого будут составлены слова\n'
          'Слова должны быть не короче 3 букв')

    # валидация слова от пользователя
    while True:
        user_word = input().lower().strip()
        if 2 < len(user_word) < 20 and user_word.isalpha() \
                and all([latter in config.RUS_ASCII_LOWERCASE for latter in user_word]):
            break
        else:
            print('Введите корректное слово')

    # выбираем откуда слова для игры будут сгенерированы
    try:
        html = get_html(user_word, headers)
        flag = True
        if html is None:  # статус код не 200
            raise models.OfflineVersion()
    except models.OfflineVersion:
        user_word, words, flag = offline_game(config.PATH_JSON)
    except Exception as e:
        print(e)
    else:
        print('Запущена онлайн версия игры (っ◕‿◕)っ ')

        # Подготавливаем слова для игры
        html_to_file(config.PATH_HTML, html)
        words = get_words(config.PATH_HTML)

    return user_word, words, flag


def offline_game(path: str) -> tuple:
    """Режим офлайн"""
    print('Запущена офлайн версия игры (っ◕‿◕)っ ')
    data = load_random_word(path)
    user_word = data['word']
    words = data['subwords']
    return user_word, words, False


def get_word_info(word: str) -> str:
    """Получаем информацию по слову из википедии"""
    url = r'https://ru.wikipedia.org/wiki/{}'.format(word.capitalize())
    request = requests.get(url)
    if request.status_code != 200:
        return config.PAGE_NOT_FOUND
    soup = BeautifulSoup(request.text, 'html.parser')
    res = soup.find('p').text.strip()
    # пример употребления слова
    if len(res.split()) < 2:
        res = soup.find('ul').text.strip()
    # обработка текста
    res = res.replace('\xa0', ' ').replace('\u200e', '')
    res = re.sub(r'[\n\r\f\v\t]', ' ', res)
    res = re.sub(r'\[\w+\]', '', res)
    return res


def grab_info(word: str, headers: dict) -> str:
    """Получаем информацию по слову"""
    url = r'https://wordhelp.ru/word/{}'.format(word.lower())
    request = requests.get(url, headers=headers)
    if request.status_code != 200:
        return config.PAGE_NOT_FOUND
    soup = BeautifulSoup(request.text, 'html.parser')

    # нужно ловить еще исключения, я не знаю какие, нужно тестить функцию
    try:
        res = soup.find("blockquote").text.strip()
    except AttributeError:
        print(f'Пример употребления слова {word.upper()}:')
        res = soup.find(class_="quote").text.strip()
    except Exception as e:
        print(e)
        return config.PAGE_NOT_FOUND
    # обработка текста
    res = re.sub(r'[\n\r\f\v\t]', ' ', res)
    return res


if __name__ == '__main__':
    pass
