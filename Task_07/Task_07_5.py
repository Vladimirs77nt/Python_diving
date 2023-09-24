# Задание 5

# ✔ Доработаем предыдущую задачу. 
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями. 
# ✔ Расширения и количество файлов функция принимает в качестве параметров. 
# ✔ Количество переданных расширений может быть любым. 
# ✔ Количество файлов для каждого расширения различно. 
# ✔ Внутри используйте вызов функции из прошлой задачи.

import os
os.chdir("Task_07/file_2")

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
        print (file_name)
        with open(file_name, "w", encoding="utf-8") as f:
            # f.write (str(random.randint(0, 1_000_000)))
            print (f" -- файл {file_name} записан --")

def generaor_file_many (**kwargs):
    for file_exp, count in kwargs.items():
        generaor_file (file_exp, count)


# ---------- ЗАПУСК ПРОГРАММЫ -------------
generaor_file_many (txt=5, doc=6, cdr=2, apx=1)