# Задание 5

# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое
# в виде одноимённых pickle файлов.

import json
import pickle
import os


# чтение рабочего файла JSON -> передача инфы в словарь: json_dict
def load_data_json (file_json) -> dict:
    if os.path.exists(file_json):
        with open (file_json, "r", encoding='utf-8') as f:
            json_dict = json.load(f)
    else:
        json_dict = {}
    return json_dict


# чтение рабочего каталога и поиск файлов с расширением .json
# состовляем список названий найденных файлов
def find_json_file (dir_path) -> list:
    file_list = []
    for files in os.walk(dir_path):
        for file in files[2]:
            if file.endswith (".json"):
                file_list.append(file)
    return file_list


def convert_json_to_pickle (dir_path):
    file_list_json = find_json_file (dir_path)
    for file_json in file_list_json:
        data_json = load_data_json (file_json)
        file_pickle = file_json.replace(".json", ".pickle")

        with open (file_pickle, "wb") as f:
            pickle.dump(data_json,f)
            print (f" >> файл {file_pickle} - записан! <<<")


# ---------- ЗАПУСК ПРОГРАММЫ -------------
dir_path = "E:/codes/Task_08"    # <-- рабочая папка с файлами
os.chdir(dir_path)

convert_json_to_pickle (dir_path)