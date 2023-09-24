# Задание 4

# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

import os
os.chdir("Task_07/file")

import random
import string

SIZE_NAME_MIN = 6
SIZE_NAME_MAX = 30
SIZE_BYTE_MIN = 256
SIZE_BYTE_MAX = 4096
COUNT_FILE = 42

letter = string.ascii_lowercase

def generate_name ():
    size = random.randint (SIZE_NAME_MIN, SIZE_NAME_MAX)
    name = ""
    for i in range (size):
        name += random.choices(list(letter))[0]
    name = "".join (name)
    return name

def generaor_file (file_exp, count=COUNT_FILE):
    for i in range(count):
        file_name = (f"{i}_{generate_name()}.{file_exp}")
        with open(file_name, "w", encoding="utf-8") as f:
            f.write (str(random.randint(0, 1_000_000)))
            print (f" -- файл {file_name} записан --")

# ---------- ЗАПУСК ПРОГРАММЫ -------------
generaor_file ("txt")