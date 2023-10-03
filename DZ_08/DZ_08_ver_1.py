# ЗАДАЧА

# * Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle. 
# ○ Для дочерних объектов указывайте родительскую директорию. 
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
#   с учётом всех вложенных файлов и директорий.


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
def write_json_csv_pickle (_result_dict, file_name):

    file_json = file_name + ".json"
    # запись JSON
    with open(file_json, 'w', encoding='utf-8') as f:
        json.dump(_result_dict, f, indent=4, ensure_ascii=False)

    # запись CSV
    file_csv = file_name + ".csv"
    data = [["Folder", "Files"]]
    for key, value in _result_dict.items():
        data.append([key, value])
    with open(file_csv, "w", encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect="excel", delimiter=";", lineterminator="\n")
        csv_write.writerows(data)

    # запись PICKLE
    file_pickle = file_name + ".pickle"
    with open(file_pickle, 'wb') as f:
        pickle.dump(_result_dict, f)



# ---------- ЗАПУСК ПРОГРАММЫ -------------
dir_path = os.getcwd() + "/DZ_06"    # <-- рабочая папка для работы
print (dir_path)

result, *_ = info_dir_and_file (dir_path)
print ("--РЕЗУЛЬТАТ--")
for key, value in result.items():
    print (key)
    for file in value:
        print (file)

dir_path = os.getcwd() + "/DZ_08"    # <-- рабочая папка для записи
file_name = "result_scan_1"
os.chdir(dir_path)
write_json_csv_pickle (result, file_name)