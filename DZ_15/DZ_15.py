# ИТОГОВОЕ ДОМАШНЕЕ ЗАДАНИЕ:

# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
#   ○ имя файла без расширения или название каталога
#   ○ расширение, если это файл,
#   ○ флаг каталога, ○ название родительского каталога.

# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
import json
import csv
import pickle


# функция рекурсивного обхода папок и файлов
def info_dir_and_file (dir_path, result_list={}, size=0):

    data_dir = os.listdir (dir_path)    # получаем список папок и файлов в обследуемой папке
    list_dir = []       # список папок
    list_file = []      # список файлов
    for i in data_dir:
        _file = dir_path + "/" + i
        if os.path.isfile(_file):
            list_file.append (_file)    # сюда складываем файлы
        else:
            list_dir.append (_file)     # сюда складываем папки
    
    # обход папок
    for _dir in list_dir:
        result_list, _size = info_dir_and_file (_dir, result_list)
        size += _size

    # обход файлов внутри папки
    temp_list = []
    for i_file in list_file:
        i_size = os.path.getsize(i_file)
        file_info = f" - Файл {i_file}, размер {i_size} байт"
        file_info = file_info.replace ("\\","/")
        temp_list.append (file_info)
        size += i_size
    dir_info = f"> Папка {os.path.abspath(dir_path)}, размер {size} байт"
    dir_info = dir_info.replace ("\\","/")
    result_list [dir_info] = temp_list
    return result_list, size


# функция записи словаря с результатами в три формата: JSON, CSV, PICKLE
def write_json (_result_dict, file_name):
    file_json = file_name + ".json"
    # запись JSON
    with open(file_json, 'w', encoding='utf-8') as f:
        json.dump(_result_dict, f, indent=4, ensure_ascii=False)


# ---------- ЗАПУСК ПРОГРАММЫ -------------
dir_path = os.getcwd() + "/DZ_15"    # <-- рабочая папка для работы
print (dir_path)

result, *_ = info_dir_and_file (dir_path)
print ("--РЕЗУЛЬТАТ--")
for key, value in result.items():
    print (key)
    for file in value:
        print (file)

dir_path = os.getcwd() + "/DZ_15"    # <-- рабочая папка для записи
file_name = "result_scan_ВОВА"
os.chdir(dir_path)
write_json (result, file_name)