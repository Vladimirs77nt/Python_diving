# Задание 6

# ✔ Дорабатываем функции из предыдущих задач. 
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции. 
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции 
# (добавьте проверки). 
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import os
import random
import string

SIZE_NAME_MIN = 6
SIZE_NAME_MAX = 30
SIZE_BYTE_MIN = 256
SIZE_BYTE_MAX = 4096
COUNT_FILE = 42

letter = string.ascii_lowercase

# инициализация рабочей папки
def init (_dir):
    default_path = os.getcwd()
    dir_path = default_path + _dir
    dir_path = dir_path.replace("\\","/")
    try:
        os.chdir(dir_path)
    except:
        os.mkdir(dir_path)
        os.chdir(dir_path)

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

# функция генерирует файлы по входящим расширениям с указанием кол-ва файлов
# первым аргументом указывается рабочая папка !!!
def generate_many_file (_dir, **kwargs):
    init (_dir)

    for file_exp, count in kwargs.items():
        generate_file (file_exp, count)


# ---------- ЗАПУСК ПРОГРАММЫ -------------
dir_path = "/DZ_07/files"    # <-- рабочая папка с файлами

# запуск генерации файлов
generate_many_file (dir_path, mov=2, mp4=3, avi=5, txt=5, doc=6, cdr=2, jpg=3, tiff=4, gif=2, svg=3, ai=10, twg=10, ght=5, vbn=8)