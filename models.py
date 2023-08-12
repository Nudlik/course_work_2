class BasicWord:
    """Класс для хранения слов"""
    def __init__(self, original_word: str, set_subwords: list):
        self.original_word = original_word
        self.set_subwords = set_subwords

    def in_subwords(self, word: str) -> bool:
        """Проверяем, есть ли слово в списке подслов"""
        return word in self.set_subwords

    def num_subwords(self) -> int:
        """Получаем количество подслов"""
        return len(self.set_subwords)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.original_word}, {self.set_subwords})'


class Player:
    """Класс для хранения игрока"""
    def __init__(self, name: str, user_words_used: list):
        self.name = name
        self.user_words_used = user_words_used

    def get_numr_words_used(self) -> int:
        """Получаем количество использованных слов"""
        return len(self.user_words_used)

    def add_word(self, word: str) -> None:
        """Добавляем слово в список использованных"""
        self.user_words_used.append(word)

    def check_used_word(self, word: str) -> bool:
        """Проверяем, есть ли слово в списке использованных"""
        return word in self.user_words_used

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.user_words_used})'


class OfflineVersion(Exception):
    """Игра оффлайн"""
    pass


class JsonFileNotFound(Exception):
    """ Json файл не найден """
    pass


class HthmlFileNotFound(Exception):
    """ HTML файл не найден """
    pass
