import config
import utils
import os


if __name__ == '__main__':

    assert os.path.exists(config.PATH_HTML) is True, 'Файл не найден'
    assert os.path.exists(config.PATH_JSON) is True, 'Файл не найден'
    assert utils.grab_info('слово', config.HEADERS) != config.PAGE_NOT_FOUND, 'Страница не найдена'
    assert utils.get_word_info('слово') != config.PAGE_NOT_FOUND, 'Страница не найдена'

    print('тесты выполнены')

