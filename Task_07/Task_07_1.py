# Задание 1

# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел. 
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000. 
# Количество строк и имя файла передаются как аргументы функции. 

import os
import random

def save_file (row, file_name):
    with open(file_name, "a", encoding="utf-8") as f:
        for _ in range (row):
            num_1 = random.randint (-1000, 1000)
            num_2 = random.uniform (-1000, 1000)
            str = (f"{num_1} | {num_2}\n")
            f.write(str)
    print (" -- файл записан --")

os.chdir("Task_07")
save_file (5, "Task_07_1_number.txt")