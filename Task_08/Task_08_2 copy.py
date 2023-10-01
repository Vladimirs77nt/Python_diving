# Задание 2

# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и
# уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

import json
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

# проверка ID в базе
def check_ID (json_dict: dict, num_id: int):
    for users in json_dict.values():
        for _id in users.keys():
            if num_id == _id:
                return True
    return False

def input_id(json_dict: dict):
    while True:
        id_number = input ("Введите ID номер: ")
        if not id_number.isdigit():
            print (" >>> Требуется ввести целое число. Введите ID повторно...")
        elif check_ID (json_dict, int (id_number)):
            print (" >>> Такой ID уже есть в системе. Введите ID повторно...")
        else:
            return int(id_number)
        
def input_access(_min, _max):
    while True:
        access_level = input (f"Введите уровень доступа ({_min}-{_max}): ")
        if not access_level.isdigit():
            print (" >>> Требуется ввести целое число. Введите уровень доступа повторно повторно...")
        elif not (_min <= int(access_level) <= _max):
            print (" >>> Уровень доступа выбран неверно! Введите уровень доступа повторно повторно..")
        else:
            return int(access_level)

def add_user (json_dict: dict):
    while True:
        print (json_dict)
        name = input ("Введите имя пользователя: ")
        if not name:
            print (" -- программа завершена --\n")
            return json_dict
        
        id_number = input_id(json_dict)
        access_level = input_access (1, 7)

        if access_level in json_dict.keys():
            json_dict[access_level][id_number] = name
        else:
            json_dict[access_level] = {id_number: name}
        save_data (json_dict)

# чтение рабочего файла JSON -> передача инфы в словарь: json_dict
def load_data (file_data) -> dict:
    if os.path.exists(file_data):
        with open (file_data, "r", encoding='utf-8') as f:
            json_dict = json.load(f)
        json_dict_new = {}
        for access_level, users in json_dict.items():
            _users = {}
            for _id, _name in users.items():
                    _users[int(_id)] = _name
            json_dict_new[int(access_level)] = _users
    else:
        json_dict_new = {}
    return json_dict_new

# запись рабочего файла JSON -> передача инфы из словаря: json_dict
def save_data (json_dict):
    with open (file_data, "w", encoding='utf-8') as f:
            json.dump(json_dict, f, indent=4, ensure_ascii=False)
    return

# ---------- ЗАПУСК ПРОГРАММЫ -------------
dir_path = "E:/codes/Task_08"    # <-- рабочая папка с файлами
init (dir_path)

file_data = "data_json.json"
json_dict = load_data (file_data)
add_user (json_dict)