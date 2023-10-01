# Задание 3

# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

import json
import csv
import os

# инициализация рабочей папки
def init (_dir):
    # default_path = os.getcwd()
    # dir_path = default_path + _dir
    try:
        os.chdir(dir_path)
    except:
        os.mkdir(dir_path)
        os.chdir(dir_path)

# чтение рабочего файла JSON -> передача инфы в словарь: json_dict
def load_data_json (file_json) -> dict:
    if os.path.exists(file_json):
        with open (file_json, "r", encoding='utf-8') as f:
            json_dict = json.load(f)
    else:
        json_dict = {}
    return json_dict

# запись рабочего файла CSV -> передача инфы из словаря: json_dict
def save_data_csv (json_dict, file_csv):
    results = []
    for access, users in json_dict.items():
        for _id, _name in users.items():
            results.append([access,_id,_name])
    print (results)

    with open (file_csv, "w", encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect="excel", delimiter="\t", lineterminator="\n")
        csv_write.writerows(results)


# ---------- ЗАПУСК ПРОГРАММЫ -------------
dir_path = "E:/codes/Task_08"    # <-- рабочая папка с файлами
init (dir_path)

file_json = "data_user.json"

file_csv = "data_user.csv"

json_dict = load_data_json (file_json)
save_data_csv (json_dict, file_csv)