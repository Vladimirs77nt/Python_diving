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
os.chdir("Task_07/file")    # <-- рабочая папка с файлами

import random
import string

SIZE_NAME_MIN = 6
SIZE_NAME_MAX = 30
SIZE_BYTE_MIN = 256
SIZE_BYTE_MAX = 4096
COUNT_FILE = 42

letter = string.ascii_lowercase

# функция генерирует случайное имя:
# SIZE_NAME_MIN - минимальное кол-во букв в имени
# SIZE_NAME_MAX - максимальнео кол-во букв в имени
def generate_name ():
    size = random.randint (SIZE_NAME_MIN, SIZE_NAME_MAX)
    name = ""
    for i in range (size):
        name += random.choices(list(letter))[0]
    name = "".join (name)
    return name

# функция генерирует файлы со случайным именем, с заданным расширением и кол-вом
def generate_file (file_exp, count=COUNT_FILE):
    for _ in range(count):
        file_name = (f"{generate_name()}.{file_exp}")
        with open(file_name, "wb") as f:
            size_file = random.randint (SIZE_BYTE_MIN, SIZE_BYTE_MAX)
            random_bytes = random.randbytes(size_file)
            f.write (random_bytes)
            print (f" -- файл {file_name:.<42}({size_file} байт) \t записан --")
    print (" << программа завершенна >>")


# ---------- ЗАПУСК ПРОГРАММЫ -------------
# запуск генерации файлов, в кол-ве указанном во втором аргументе

generate_file ("doc", 5)