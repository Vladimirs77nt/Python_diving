# Задание 1

# Вспоминаем задачу 3 из прошлого семинара.
# Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.

import os
import json


# инициализация рабочей папки
def init (_dir):
    # default_path = os.getcwd()
    # dir_path = default_path + _dir
    try:
        os.chdir(dir_path)
    except:
        os.mkdir(dir_path)
        os.chdir(dir_path)

# функция чтения списка из указанного текстового файла
def load_file (file):
    list_file = []
    with open(file, "r", encoding="utf-8") as f:
        for str in list(f):
            list_file.append (str[:-2])
    print (f" -- файл {file} прочитан --")  
    return list_file

def function (file_text, file_json):
    dict_file = {}
    with open(file_text, "r", encoding="utf-8") as f:
        for str in list(f):
            line = str.strip().split()
            dict_file [line[0].title()] = line [1]
    with open(file_json, 'w') as f:
        json.dump(dict_file, f, indent=4)
    print (f" -- файл {file_json} записан --")  
    return dict_file

# ---------- ЗАПУСК ПРОГРАММЫ -------------
dir_path = "E:/codes/Task_08"    # <-- рабочая папка с файлами
init (dir_path)

file_text = "../Task_07/Task_07_3_muli_name.txt"
file_json = "Task_08_1_json.json"

# запуск

print (function (file_text, file_json))

print (" << программа завершенна >>")