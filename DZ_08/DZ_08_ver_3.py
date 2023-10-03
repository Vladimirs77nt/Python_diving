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

def info_dir_and_file (dir_path):
    # готовим словарь
    result_dict = {}
    for _dir, _folder, _file in os.walk(dir_path):
        dir_size = 0        # размер папки с файлами
        list_file_name = [] # список файлов в папке
        for i_file in _file:
            full_path = _dir + "\\" + i_file
            i_size = os.path.getsize(os.path.abspath(full_path))
            data_file_str = f" - файл {i_file} ({_dir}, размер {i_size} байт)"
            list_file_name.append (data_file_str)
            dir_size += i_size

        data_folder_str = f' > Папка: {_dir} ({dir_size} байт)'
        result_dict[data_folder_str] = list_file_name

    return result_dict
    

# функция записи словаря с результатами в три формата: JSON, CSV, PICKLE
def write_json_csv_pickle (_result_dict, file_name):

    file_json = file_name + ".json"
    # запись JSON
    with open(file_json, 'w', encoding='utf-8') as f:
        json.dump(_result_dict, f, indent=4, separators=(',', ':'))

    # запись CSV
    file_csv = file_name + ".csv"
    data = [["Folder", "Files"]]
    for key, value in _result_dict.items():
        data.append([key, value])
    with open(file_csv, "w", encoding='CP1251') as f:
        csv_write = csv.writer(f, dialect="excel", delimiter=";", lineterminator="\n")
        csv_write.writerows(data)

    # запись PICKLE
    file_pickle = file_name + ".pickle"
    with open(file_pickle, 'wb') as f:
        pickle.dump(_result_dict, f)



# ---------- ЗАПУСК ПРОГРАММЫ -------------
dir_path = "E:/codes/DZ_06"    # <-- рабочая папка для сканирования паплк и файлов
os.chdir(dir_path)
print (dir_path)

result = info_dir_and_file (dir_path)
print ("--РЕЗУЛЬТАТ--")
for key, value in result.items():
    print (key)
    for file in value:
        print (file)

dir_path = "E:/codes/DZ_08"    # <-- рабочая папка для записи
file_name = "result_scan_3"
os.chdir(dir_path)
write_json_csv_pickle (result, file_name)