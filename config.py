import os


# Заголовки для запроса
HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate, lzma, sdch',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
}

# Пути к файлам
PATH_HTML = os.path.join(os.path.dirname(__name__), 'data', 'web_page.html')
PATH_JSON = os.path.join(os.path.dirname(__name__), 'data', 'offline_data.json')

# Русские буквы
RUS_ASCII_LOWERCASE = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Страница не найдена
PAGE_NOT_FOUND = 'Страница не найдена'

if __name__ == '__main__':
    pass
