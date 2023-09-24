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

def generaor_file_many (_dir, **kwargs):
    try:
        os.chdir(_dir)
    except:
        os.mkdir(_dir)

    os.chdir(_dir)
    for file_exp, count in kwargs.items():
        generaor_file (file_exp, count)


# ---------- ЗАПУСК ПРОГРАММЫ -------------

default_path = os.getcwd()
dir_path = default_path + "/Task_07/file_4"
dir_path = dir_path.replace("\\","/")
print (dir_path)
generaor_file_many (dir_path, mov=2, mp4=3, avi=5, txt=5, doc=6, cdr=2, jpg=3, tiff=4, gif=2, twm=3, apx=1)