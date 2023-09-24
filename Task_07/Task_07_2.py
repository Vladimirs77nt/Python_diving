# Задание 2

# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные. 
# Полученные имена сохраните в файл.

import os
import random
import string

letter = string.ascii_lowercase
vowels = "eyuioa"

def generate_name ():
    size = random.randint (4, 7)
    name = random.sample (letter, size-1)
    name.append (random.choice(vowels))
    random.shuffle(name)
    name = "".join (name).title()
    return name

def save_to_file (count, file_name):
    with open(file_name, "a", encoding="utf-8") as f:
        for _ in range (count):
            name = generate_name ()
            str = (f"{name}\n")
            f.write(str)
    print (" -- файл записан --")    


# ---------- ЗАПУСК ПРОГРАММЫ -------------
os.chdir("Task_07")
save_to_file (5, "Task_07_2_name.txt")




# изначальны пробный вариант....
# import random

# list_1 = [chr(i) for i in range(1040, 1072)]    # заглавные буквы
# list_2 = [chr(i) for i in range(1072, 1104)]    # строчные буквы

# def create_name ():
#     lens = random.randint (4, 7)
#     name = random.choice(list_1)
#     for _ in range (lens-1):
#         name += random.choice(list_2)
#     return name

# print (create_name ())