# Задание 5

# ✔ Доработаем предыдущую задачу. 
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями. 
# ✔ Расширения и количество файлов функция принимает в качестве параметров. 
# ✔ Количество переданных расширений может быть любым. 
# ✔ Количество файлов для каждого расширения различно. 
# ✔ Внутри используйте вызов функции из прошлой задачи.

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
def generate_many_file (**kwargs):
    for file_exp, count in kwargs.items():
        generate_file (file_exp, count)
    print (" << программа завершенна >>")


# ---------- ЗАПУСК ПРОГРАММЫ -------------
dir_path = "/Task_07/file_2"    # <-- рабочая папка с файлами
init (dir_path)

# запуск генерации файлов
generate_many_file (txt=2, doc=8, cdr=5, apx=3, jpg=3, png=3, tmp=3)