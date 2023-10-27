# ИТОГОВОЕ ДОМАШНЕЕ ЗАДАНИЕ:

# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
#   ○ имя файла без расширения или название каталога
#   ○ расширение, если это файл,
#   ○ флаг каталога, ○ название родительского каталога.

# В процессе сбора сохраните данные в текстовый файл используя логирование.

# ВНИМАНИЕ !!! ИСХОДНИК МОДУЛЯ - ОТ СТОУНА !!!


import os
import sys
from pprint import pprint
import json


def size_of_dir(dir_path: str) -> int:
    total_size = 0
    for path, _, files in os.walk(dir_path):
        for file in files:
            total_size += sys.getsizeof(os.path.join(path, file))
            print (file, "=", sys.getsizeof(os.path.join(path, file)))
    return total_size

def json_writer(current_path: str, source = dict[str, dict]):
    file_name_json = file_name + ".json"
    with open (file_name_json, "w", encoding="utf-8") as date:
        json.dump(source, date, indent=4, ensure_ascii=False)


def dir_walker(full_path: str = os.getcwd()):
    result = {}
    for path, dir_list, file_list in os.walk(full_path):
        for cur_dir in dir_list:
            result[os.path.join(path, cur_dir)] = {"name": cur_dir,
                                                   "path": str(path),
                                                   "type": "DIR",
                                                   "size": size_of_dir(os.path.join(path, cur_dir))}
        for cur_file in file_list:
            result[os.path.join(path, cur_file)] = {"name": cur_file,
                                                   "path": path,
                                                   "type": "FILE",
                                                   "size": os.path.getsize(os.path.join(path, cur_file))}
    return result


# --------------- ЗАПУСК ПРОГРАММЫ ------------------

print ()
print (" --- ВНИМАНИЕ !!! ЗАДАЧА ЕЩЕ В ПРОЦЕССЕ РЕШЕНИЯ !!! ---")
print ()

base_dir_path = os.getcwd()
dir_path = base_dir_path + "/DZ_06"    # <-- рабочая папка для записи
os.chdir(dir_path)
result = dir_walker(dir_path)
pprint (result)

dir_path = base_dir_path + "/DZ_15"    # <-- рабочая папка для записи
file_name = "result_scan_СТОУН"
os.chdir(dir_path)
json_writer(file_name, result)

print ()
print (" --- ВНИМАНИЕ !!! ЗАДАЧА ЕЩЕ В ПРОЦЕССЕ РЕШЕНИЯ !!! ---")
print ()