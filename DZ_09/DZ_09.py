# Задание

# Напишите следующие функции:
# 1. Нахождение корней квадратного уравнения
# 2. Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# 3. Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# 4. Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

from typing import Callable
from functools import wraps
import random
import csv
import json
import os


# --- ДЕКОРАТОР №1 -> для чтения параметров из csv файла ---
def decor_csv_reader (func: Callable):
    def wrapper (*args):
        result = []
        with open (file_name_csv, "r", encoding='CP1251') as f:
            csv_data = csv.reader (f, dialect="excel", delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
            for line in csv_data:
                a, b, c, *_ = line
                roots = func (a, b, c)
                result.append (roots)
        return result
    return wrapper


# --- ДЕКОРАТОР №2 -> для записи параметров и результатов в JSON файл ---
def decor_json_param (func: Callable):
    data = {}
    def wrapper (*args, **kwargs):
        a, b, c = args
        result = func (a, b, c)
        key = f"{a}, {b}, {c}"
        data [key] = result
        with open (file_name_json, "w", encoding="utf-8") as file:
            json.dump (data, file, indent=4, ensure_ascii=False )
        return result
    return wrapper


#-------------------------------------------------------------------------------------------
# функция генерирует строчки по 3 числа (от 100 до 1000 строчек) и записываем в csv-файл
def csv_generator_3_num (file_name):
    rows = random.randint(100,1001)
    result = []
    for _ in range (rows):
        line = [random.randint(1,100), random.randint(-100,100), random.randint(-100,100)]
        result.append (line)
    # специально выбираю кодировку CP1521 и delimiter=";" для Excel
    with open (file_name, "w", encoding='CP1251') as f:
        csv_write = csv.writer(f, dialect="excel", delimiter=";", lineterminator="\n")
        csv_write.writerows(result)
    return result


#-------------------------------------------------------------------------------------------
@decor_csv_reader   # декоратор 1 <-- чтение CSV файла с передачей аргументов на к функции
@decor_json_param   # декоратор 2 --> запись JSON (аргументы и результат вычисления)
def roots_quadratic_equation (*args):
    a, b, c = args
    disc = b*b - 4*a*c
    if disc < 0:
        return "-- НЕТ РЕШЕНИЯ --"
    if disc >0:
        x1 = (-b + disc**0.5)/(2*a)
        x2 = -x1
        return x1, x2
    return -b/(2*a)


# ------------------ БЛОК ЗАПУСКА ---------------------
dir_path = os.getcwd() + "/DZ_09"   # <-- рабочая папка для записи и чтения файлов
os.chdir(dir_path)

file_name_csv = "data.csv"              # задаем имя для рабочего csv-файла
print (f" -- генерация файла CSV ({file_name_csv}) с рядами по 3 случайных числа")
csv_generator_3_num (file_name_csv)     # генерируем много строчек по 3 числа и записываем в csv-файл

file_name_json = file_name_csv.replace (".csv", ".json")
print (f" -- генерация файла JSON ({file_name_json}) результатом вычисления корней")
roots_quadratic_equation ()         # ищем корни по аргументам из csv-файле - записываем в JSON