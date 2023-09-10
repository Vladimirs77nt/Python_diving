# Задание №1

# ✔ Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

import re

def function (text):
    text = re.sub(r'[^\w\s]','',text.lower())  # убираем все знаки пунктуации (используя регулярные выражения)
    text = ' '.join(text.split())              # убираем лишние пробелы
    text = sorted(text.split())                # сплитуем и сортируем
    len_max = len(max(text, key=len))
    for i, j in enumerate (text):
        print(f"{i+1:>3}. {j:>{len_max}}")

text = "Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки. яяяяяяяяяяяяяяяяяяя"
function (text)