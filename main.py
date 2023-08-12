import utils
import models
import config
from pprint import pprint as pp


def main():
    """Основная программа"""
    print('Ввведите имя игрока:')
    user_name = input().capitalize().strip()
    print(f'Привет, {user_name}!')

    print('Выберите режим игры:\n1 - Онлайн\n2 - Оффлайн')
    while True:
        hard = input()
        if hard not in ('1', '2'):
            print('Введите число 1 или 2')
        else:
            flag = True if hard == '1' else False
            break

    # Выбираем режим игры
    user_word, words, flag = utils.online_game(config.PATH_JSON, config.HEADERS) if flag \
        else utils.offline_game(config.PATH_JSON)

    # print(words)  # список генерируемых (слов с сайта \ слов из джсон) для тестов :)
    print(f'Для генерации списка взято слово - {user_word.upper()}\n'
          f'Слов сгенерированно: {len(words)}\n'
          f'Подсказка: если набрать слово с ? в конце, например: слово? \\ жираф? \\ фарт? - '
          'такая конструкция вернет значение слова из википедии\n'
          f'Подсказка: один знак ? в поле ввода - вернет загаданное слово\n'
          f'Чтобы закончить игру, угадайте все слова или напишите: "stop" \\ "стоп"\n'
          'Поехали, ваше первое слово?')

    # классификация
    player = models.Player(user_name, [])
    words = models.BasicWord(user_word, words)

    while True:
        user_input = input().lower().strip()

        if user_input in ('stop', 'стоп'):
            break

        # реализация варианта с '?'
        if user_input.endswith('?') and user_input[:-1].isalpha():
            pp(utils.get_word_info(user_input[:-1]))
            continue
        elif user_input == '?':
            print(f'Вы загадали слово: {user_word.upper()}')
            continue

        if player.check_used_word(user_input):
            print('Уже использовано')
        # если режим 1 выводить доп. инфу с сайта
        elif flag and words.in_subwords(user_input):
            player.add_word(user_input)
            print('Верно:')
            pp(f'{utils.grab_info(user_input, config.HEADERS)}')
        elif words.in_subwords(user_input):
            player.add_word(user_input)
            print('Верно')

            # 2ая вариация завершения цикла
            if words.num_subwords() == player.get_numr_words_used():
                break
        else:
            print('Неверно')

    print(f'Игра завершена, вы угадали {player.get_numr_words_used()} слов!')


if __name__ == '__main__':
    main()
