# ИТОГОВОЕ ДОМАШНЕЕ ЗАДАНИЕ:

# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
#   ○ имя файла без расширения или название каталога
#   ○ расширение, если это файл,
#   ○ флаг каталога, ○ название родительского каталога.

# В процессе сбора сохраните данные в текстовый файл используя логирование.


# ВНИМАНИЕ !!! ИСПОЛЬЗУЕТСЯ ИСХОДНИК МОДУЛЯ ОТ СТОУНА !!!

import os
from collections import namedtuple
import argparse
import logging


def size_of_dir(dir_path: str) -> int:
    total_size = 0
    for path, _, files in os.walk(dir_path):
        for file in files:
            total_size += os.path.getsize(os.path.join(path, file))
    return total_size

def dir_walker(full_path: str = os.getcwd()):
    nametuple_list=[]
    # (1) инициализация для объектов namedtuple
        # [0] Name          - имя файла/папки
        # [1] Extension     - расширение файла (или None)
        # [2] is_Folder True/False  - флаг папки
        # [3] Parent_folder - родительская папка
        # [4] Size          - размер папки или файла
    dct = {"Name": "", "Extension": "", "is_Folder": False, "Parent_folder": "", "Size": 0}
    Result_tuple = namedtuple("Result_tuple", dct)

    for path, dir_list, file_list in os.walk(full_path):
        path = path.replace ("\\","/")
        for cur_dir in dir_list:
            size_dir = size_of_dir(os.path.join(path, cur_dir))
            nametuple_dir = Result_tuple (cur_dir, None, True, path, size_dir)
            nametuple_list.append (nametuple_dir)
            logger.info(msg=nametuple_to_json_str(nametuple_dir))

        for cur_file in file_list:
            # магия получения имени файла, расширения и полного пути до него
            *file_name, file_extension = cur_file.split(".")   # "прааую" часть (b) сплитуем по точкам на 2 части: всю "левую" часть до последней ".", и "правую" - где только расширение
            file_name = ".".join(i for i in file_name)          # "левую" часть собираем обратно - это полное название без расширения
            size_file = os.path.getsize(os.path.join(path, cur_file))
            nametuple_file = Result_tuple (file_name, file_extension, False, path, size_file)
            nametuple_list.append (nametuple_file)
            logger.info(msg=nametuple_to_json_str(nametuple_file))

    return nametuple_list

# функция записи словаря с результатами в формат JSON
def nametuple_to_json_str (nametuple_obj):
    key = nametuple_obj[3] + "/" + nametuple_obj[0] + (f".{nametuple_obj[1]}" if nametuple_obj[1] else "")
    json_str = f"{key}:\n\
        \tName: {nametuple_obj[0]},\n\
        \tExtension: {nametuple_obj[1]},\n\
        \tis_Folder: {nametuple_obj[2]},\n\
        \tParent_folder: {nametuple_obj[3]},\n\
        \tSize: {nametuple_obj[4]}\n"
    return json_str


# --------------- ЗАПУСК ПРОГРАММЫ ------------------

print ()
print (" --- ВНИМАНИЕ !!! В ДАННОМ РЕШЕНИИ ИСПОЛЬЗУЕТСЯ ЛОГИКА ОБХОДА ПАПОК ОТ СТОУНА ---")
print (" ---  os.walk(full_path): ---")
print (" ----- ЗАПИСЬ РЕЗУЛЬТАТА В LOG-ФАЙЛ -----")
print ()

# НАСТРОЙКА ЗНАЧЕНИЙ ПО УМОЛЧАНИЮ
dir_path_base = "E:/codes"               # <-- полный путь к текущей рабочей папке со всеми программами курса "Погружение..."
dir_path_in = dir_path_base + ""         # <-- рабочая папка для сканирования папок и файлов
dir_path_out = dir_path_base + "/DZ_15"  # <-- рабочая папка для записи файла логирования
file_name_out = "logfile_СТОУН.log"            # <-- название для файла логирования

# НАСТРОЙКА ПАРСЕРА
parser = argparse.ArgumentParser(description='Сбор информации о папках и файлах по указанному пути')
parser.add_argument("-indir", metavar='indir', type=str, nargs = 1, default=dir_path_in,
                    help=f"- введите полный путь к обследуемой папки (defajult = {dir_path_in})")
parser.add_argument("-outdir",  metavar='outdir', type=str, nargs = 1, default=dir_path_out,
                    help=f"- введите полный путь к папке для записи файла логирования (default = {dir_path_out})")
parser.add_argument("-logfile",  metavar='logfile', type=str, nargs = 1, default=file_name_out,
                    help=f"- введите название файла логирования (default = {file_name_out})")
args = parser.parse_args()

dir_path_in = args.indir
if type(dir_path_in) == list:
    dir_path_in, *_ = args.indir

dir_path_out = args.outdir
if type(dir_path_out) == list:
    dir_path_out, *_ = args.outdir

file_name_out = args.logfile
if type(file_name_out) == list:
    file_name_out, *_ = args.logfile

# НАСТРАИВАЕМ ЛОГИРОВАНИЕ
logger = logging.getLogger(__name__)
my_format = '{msg}'
logging.basicConfig(filename=f"{dir_path_out}/{file_name_out}", filemode="w", encoding='UTF-8',
                    level=logging.INFO, style='{', format=my_format)

# ПОЛУЧАЕМ результат (и полный размер обследуемой папки)
print (f" > обработка запущена для папки {dir_path_in}...")
result = dir_walker (dir_path_in)
print (" > ...выполнено")
print (f" > записан лог-файл {file_name_out}.json в папке: {dir_path_out}")
print ()