# ИТОГОВОЕ ДОМАШНЕЕ ЗАДАНИЕ:

# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
#   ○ имя файла без расширения или название каталога
#   ○ расширение, если это файл,
#   ○ флаг каталога
#   ○ название родительского каталога.

# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
import json
from collections import namedtuple
import pprint


# функция рекурсивного обхода папок и файлов
def info_dir_and_file (dir_path, nametuple_list=None, size=0):

    if nametuple_list is None:    # ИНИЦИАЛИЗАЦИЯ ДЛЯ ОБЪЕКТОВ namedtuple
        dir_path = dir_path.replace ("\\","/")
        dct = {"Name": "", "Extension": "", "is_Folder": False, "Parrent_folder": "", "Size": 0}
        Result_tuple = namedtuple("Result_tuple", dct)
        nametuple_list = []
        print (f" >>> ИНИЦИАЛИЗАЦИЯ ДЛЯ ПАПКИ {dir_path} <<<\n")

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
        print (f" --- ОБХОД ПАПКИ {_dir} ---\n")
        nametuple_list, _size = info_dir_and_file (_dir, nametuple_list)
        size += _size

    # обход файлов внутри папки
    print (f" --- ОБХОД !ВНУТРИ! ПАПКИ {dir_path} ---\n")
    nametuple_list_file = []
    for i_file in list_file:
        i_size = os.path.getsize(i_file)    # размер файла

        # магия получения имения файла, полного пути до него и расширения
        *_, file_name = i_file.split("/")               # отбрасываем левую часть до послежней "\"
        *file_name, file_extension = file_name.split(".")   # "прааую" часть (b) сплитуем по точкам на 2 части: всю "левую" часть до последней ".", и "правую" - где только расширение
        file_name = ".".join(i for i in file_name)  # "левую" часть собираем обратно - это полное название без расширения
       
        if file_name == "": # обработка ситуации когда у файла нет расширения
            file_name = file_extension
            file_extension = "---"

        nametuple_list_file.append (Result_tuple (file_name, file_extension, False, dir_path, i_size))
        print (f" + добавлен файл {file_name} ({dir_path})")

        size += i_size  # суммируем все файлы по размеры - это размер текущей папки
    
    *dir_path, dir_name = dir_path.split("/")
    dir_path = "/".join(i for i in dir_path)

    # в итоговый список объектов добавляем информацию о папке
    nametuple_list.append (Result_tuple (dir_name, None, True, dir_path, size))
    print (f" +++ добавлена папка {dir_name} ({dir_path})")

    # после добавления объекта папки добавляем файлы, которые есть в этой папке
    nametuple_list += nametuple_list_file  

    return nametuple_list, size


# функция записи словаря с результатами в формат JSON
def write_json (_result_dict, file_name):
    file_json = file_name + ".json"
    # запись JSON
    with open(file_json, 'w', encoding='utf-8') as f:
        json.dump(_result_dict, f, indent=4, ensure_ascii=False)


# --------------- ЗАПУСК ПРОГРАММЫ ------------------

print ()
print (" --- ВНИМАНИЕ !!! ЗАДАЧА ЕЩЕ В ПРОЦЕССЕ РЕШЕНИЯ !!! ---")
print (" --- ЗАГРУЗКА БУДЕТ СДЕЛАНА СЕГОДНЯ НОЧЬЮ ИЛИ ЗАВТРА УТРОМ ---")

print ()


base_dir_path = os.getcwd()
dir_path = base_dir_path + ""    # <-- рабочая папка для обследования
os.chdir(dir_path)
print (" - Папка для обследования: ", dir_path)

result, _ = info_dir_and_file (dir_path)

print ("--РЕЗУЛЬТАТ--")
# [0] Name
# [1] Extension
# [2] is_Folder True/False
# [3] Parrent_folder
# [4] Size

for file_info in result:
    if file_info[2]:
        print (f" > Папка {file_info[0]}\n\t{file_info[3]}\n\tразмер: {file_info[4]}")
    else:
        print (f"  - файл: {file_info[0]}\n\t.{file_info[1]}\n\t{file_info[3]}\n\tразмер: {file_info[4]}")

dir_path = base_dir_path + "\DZ_15"    # <-- рабочая папка для записи
file_name = "result_scan_copy"
os.chdir(dir_path)
write_json (result, file_name)

print ()
print (" --- ВНИМАНИЕ !!! ЗАДАЧА ЕЩЕ В ПРОЦЕССЕ РЕШЕНИЯ !!! ---")
print (" --- ЗАГРУЗКА БУДЕТ СДЕЛАНА СЕГОДНЯ НОЧЬЮ ИЛИ ЗАВТРА УТРОМ ---")
print ()