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


# функция рекурсивного обхода папок и файлов
# !!! для внешнего вызова функции на входе задаем ТОЛЬКО путь к папке !!!
def scan_dir_path (dir_path, nametuple_list=[], size=0):

    # (1) инициализация для объектов namedtuple
    dct = {"Name": "", "Extension": "", "is_Folder": False, "Parent_folder": "", "Size": 0}
    Result_tuple = namedtuple("Result_tuple", dct)

    # (2) получаем список папок и файлов в обследуемой папке
    dir_path = dir_path.replace ("\\","/")
    data_dir = os.listdir (dir_path)
    list_dir = []                       # список папок
    list_file = []                      # список файлов
    for i in data_dir:
        _file = dir_path + "/" + i
        if os.path.isfile(_file):
            list_file.append (_file)    # сюда складываем файлы (list_file)
        else:
            list_dir.append (_file)     # сюда складываем папки (list_dir)
    
    # (3) РЕКУРСИВНЫЙ обход ВСЕХ папок
    # если список папок (list_dir) - пустой, то начинаем обрабатывать файлы внутри папки (4)
    for _dir in list_dir:
        nametuple_list, _size = scan_dir_path (_dir, nametuple_list)    #  <-- рекурсивный вызов функции
        size += _size   # на выходе получаем размер обследуемой папки

    # (4) обход файлов внутри папки
    nametuple_list_file = []
    for i_file in list_file:
        i_size = os.path.getsize(i_file)    # размер файла

        # магия получения имени файла, расширения и полного пути до него
        *_, file_name = i_file.split("/")                   # отбрасываем левую часть до послежней "\"
        *file_name, file_extension = file_name.split(".")   # "прааую" часть (b) сплитуем по точкам на 2 части: всю "левую" часть до последней ".", и "правую" - где только расширение
        file_name = ".".join(i for i in file_name)          # "левую" часть собираем обратно - это полное название без расширения
       
       # обработка ситуации когда у файла нет расширения
        if file_name == "":
            file_name = file_extension
            file_extension = None

        # с список добавляем объект namedtuple = файл
        nametuple_list_file.append (Result_tuple (file_name, file_extension, False, dir_path, i_size))

        # суммируем размер всех файлов в одной папке (итоговый размер папки)
        size += i_size
    
    *dir_path, dir_name = dir_path.split("/")
    dir_path = "/".join(i for i in dir_path)

    # в итоговый список объектов добавляем информацию о папке
    nametuple_list.append (Result_tuple (dir_name, None, True, dir_path, size))

    # после добавления объекта папки добавляем файлы, которые есть в этой папке
    nametuple_list += nametuple_list_file  

    # выход из рекурсии
    return nametuple_list, size


# функция записи словаря с результатами в формат JSON
def write_json (result, file_name):
    file_json = file_name + ".json"
    result_dict = {}
    for file_info in result:
        key = file_info[3] + "/" + file_info[0] + (f".{file_info[1]}" if file_info[1] else "")
        result_dict [key] = file_info._asdict()

    # запись JSON
    with open(file_json, 'w', encoding='utf-8') as f:
        json.dump(result_dict, f, indent=4, ensure_ascii=False)


# --------------- ЗАПУСК ПРОГРАММЫ ------------------

print ()
print (" --- ВНИМАНИЕ !!! ЗАДАЧА ПОЧТИ РЕШЕНА !!! ---")
print ()


base_dir_path = os.getcwd()     # <-- полный путь к текущей рабочей папке
dir_path = base_dir_path + ""   # <-- рабочая папка для обследования
os.chdir(dir_path)
print (" - Папка для обследования: ", dir_path)

# получаем результат (и полный размер обследуемой папки)
result, _ = scan_dir_path (dir_path)

print ("--РЕЗУЛЬТАТ--")
# [0] Name
# [1] Extension
# [2] is_Folder True/False
# [3] Parent_folder
# [4] Size

# for file_info in result:
#     if file_info[2]:
#         print (f" > Папка {file_info[0]}\n\t{file_info[3]}\n\tразмер: {file_info[4]}")
#     else:
#         print (f"  - файл: {file_info[0]}\n\t.{file_info[1]}\n\t{file_info[3]}\n\tразмер: {file_info[4]}")

dir_path = base_dir_path + "\DZ_15"    # <-- рабочая папка для записи
file_name = "result_scan_copy"
os.chdir(dir_path)
write_json (result, file_name)

print ()
print (" --- ВНИМАНИЕ !!! ЗАДАЧА ЕЩЕ В ПРОЦЕССЕ РЕШЕНИЯ !!! ---")
print (" --- ЗАГРУЗКА БУДЕТ СДЕЛАНА СЕГОДНЯ НОЧЬЮ ИЛИ ЗАВТРА УТРОМ ---")
print ()