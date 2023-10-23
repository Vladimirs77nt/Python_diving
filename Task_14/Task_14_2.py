# Задание №2

# Напишите для задачи 1 тесты doctest.

# Проверьте следующие варианты:
# * возврат строки без изменений
# * возврат строки с преобразованием регистра без потери символов
# * возврат строки с удалением знаков пунктуации
# * возврат строки с удалением букв других алфавитов
# * возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import doctest

from string import ascii_letters

def clear_text (text: str):
    """
    >>> clear_text ("text test") == "text test"
    True
    >>> clear_text ("TEXT TEST") == "text test"
    True
    >>> clear_text ("text-test") == "texttest"
    True
    >>> clear_text ("text РУССКИЙ test") == "text  test"
    True
    >>> clear_text ("TEXT РУССКИЙ-123-test") == "text test"
    True
    >>> clear_text ()
    Traceback (most recent call last):
    ...
    TypeError: clear_text() missing 1 required positional argument: 'text'
    >>> clear_text (1)
    Traceback (most recent call last):
    ...
    TypeError: clear_text() missing 1 required positional argument: 'text'
    """
    result = ""
    if text is None:
        raise ValueError ("Text non ")
    for i in text:
        if i in ascii_letters + " ":
            result += i
    return result.lower()


doctest.testmod(verbose=True)