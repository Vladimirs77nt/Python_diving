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
        file_info = f" - Файл {i_file}, размер {i_size} байт (папка: {dir_path})"
        file_info = file_info.replace ("\\","/")
        temp_list.append (file_info)
        size += i_size
    dir_info = f"> Папка {os.path.abspath(dir_path)}, размер {size} байт"
    dir_info = dir_info.replace ("\\","/")
    result_list [os.path.abspath(dir_path)] = {"type": "Папка",
                                               "name": dir_path,
                                               "path": dir_path,
                                               "size": sizeмм}
    return result_list, size


# функция записи словаря с результатами в формат JSON
def write_json (_result_dict, file_name):
    file_json = file_name + ".json"
    # запись JSON
    with open(file_json, 'w', encoding='utf-8') as f:
        json.dump(_result_dict, f, indent=4, ensure_ascii=False)

# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
#         - принимает на вход строку — абсолютный путь до файла.
def func_file_path (file):
    *a, b = file.split("\\")               # слитуем по "\" на 2 части: всю "левую" часть до последней "\"" - и далее до конца
    path_file = "\\".join(i for i in a)         # "левую" часть (a) сплитуем, собираем обратно - это полный путь
    # так как названия бывают с точками - определяем где последняя точка, перед расширением
    *file_name, file_extension = b.split(".")   # "прааую" часть (b) сплитуем по точкам на 2 части: 
                                                # всю "левую" часть до последней ".", и "правую" - где только расширение
    file_name = ".".join(j for j in file_name)  # "левую" часть собираем обратно - это полное название без расширения
    print ()
    print (f"            Путь:   {path_file}")
    print (f"       имя файла:   {file_name}")
    print (f"расширение файла:   {file_extension}")
    print ()


# --------------- ЗАПУСК ПРОГРАММЫ ------------------

print ()
print (" --- ВНИМАНИЕ !!! ЗАДАЧА ЕЩЕ В ПРОЦЕССЕ РЕШЕНИЯ !!! ---")
print ()


base_dir_path = os.getcwd()
dir_path = base_dir_path + "/DZ_06"    # <-- рабочая папка для работы
os.chdir(dir_path)

result, *_ = info_dir_and_file (dir_path)
print ("--РЕЗУЛЬТАТ--")
for key, value in result.items():
    print (key)
    for file in value:
        print (file)

dir_path = base_dir_path + "/DZ_15"    # <-- рабочая папка для записи
file_name = "result_scan"
os.chdir(dir_path)
write_json (result, file_name)

print ()
print (" --- ВНИМАНИЕ !!! ЗАДАЧА ЕЩЕ В ПРОЦЕССЕ РЕШЕНИЯ !!! ---")
print ()