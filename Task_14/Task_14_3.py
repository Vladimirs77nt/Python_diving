# Задание №3

# Напишите для задачи 1 тесты unittest.

# Проверьте следующие варианты:
# * возврат строки без изменений
# * возврат строки с преобразованием регистра без потери символов
# * возврат строки с удалением знаков пунктуации
# * возврат строки с удалением букв других алфавитов
# * возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import unittest

from string import ascii_letters

class TestCaseName(unittest.TestCase):
    def test_method_1 (self):
        self.assertEqual(clear_text ("text test"), "text test")
        
    def test_method_2 (self):
        self.assertEqual(clear_text ("TEXT TEST"), "text test")
    
    def test_method_3 (self):
        self.assertEqual(clear_text ("text-test"), "texttest")

    def test_method_4 (self):
        self.assertTrue(clear_text ("text РУССКИЙ test") == "text  test")

    def test_method_5 (self):
        self.assertTrue (clear_text ("TEXT РУССКИЙ-123-test") == "text test")

    def test_method_6 (self):
        self.assertRaises (TypeError, clear_text, None)


def clear_text (text: str):

    result = ""
    for i in text:
        if i in ascii_letters + " ":
            result += i
    return result.lower()

unittest.main(verbosity=2)