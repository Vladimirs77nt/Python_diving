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
import argparse


# функция рекурсивного обхода папок и файлов
# !!! для внешнего вызова функции на входе задаем ТОЛЬКО путь к папке !!!
def scan_dir_path (dir_path, nametuple_list=[], size=0):

    # (1) инициализация для объектов namedtuple
        # [0] Name          - имя файла/папки
        # [1] Extension     - расширение файла (или None)
        # [2] is_Folder True/False  - флаг папки
        # [3] Parent_folder - родительская папка
        # [4] Size          - размер папки или файла
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


# НАСТРОЙКА ЗНАЧЕНИЙ ПО УМОЛЧАНИЮ
dir_path_base = "E:/codes"               # <-- полный путь к текущей рабочей папке со всеми программами курса "Погружение..."
dir_path_out = dir_path_base + "/DZ_15"  # <-- рабочая папка для записи файла логирования
file_name_out = "result_logfile"         # <-- название для файла логирования

# НАСТРОЙКА ПАРСЕРА
parser = argparse.ArgumentParser(description='Сбор информации о папках и файлах по указанному пути')
parser.add_argument("-indir", metavar='indir', type=str, nargs = 1, default=dir_path_base,
                    help=f"- введите полный путь к обследуемой папки (defajult = {dir_path_base})")
parser.add_argument("-outdir",  metavar='outdir', type=str, nargs = 1, default=dir_path_out,
                    help=f"- введите полный путь к папке для записи файла логирования (default = {dir_path_out})")
parser.add_argument("-logfile",  metavar='logfile', type=str, nargs = 1, default=file_name_out,
                    help=f"- введите название файла логирования (default = {file_name_out})")
args = parser.parse_args()

dir_path = args.indir
if type(dir_path) == list:
    dir_path, *_ = args.indir

dir_path_out = args.outdir
if type(dir_path_out) == list:
    dir_path_out, *_ = args.outdir

file_name_out, *_ = args.logfile
if type(file_name_out) == list:
    file_name_out, *_ = args.logfile

print (" Папка для обследования:", dir_path)
os.chdir(dir_path)

# ПОЛУЧАЕМ результат (и полный размер обследуемой папки)
print (" > обработка запущена...")
result, size_dir = scan_dir_path (dir_path)
print (" > ...выполнено")

# ЛОГИРУЕМ результат
os.chdir(dir_path_out)
write_json (result, file_name_out)