# Задание №4

# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя,
# личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.

import json
import os

# класс пользователя
class User:

    def __init__(self, name, id_user, access_level):
        self.name = name
        self.id_user = id_user
        self.access_level = access_level

    def __str__ (self):
        return f"Пользователь {self.name}, ID: {self.id_user}, уровень доступа: {self.access_level}"

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
            if int(num_id) == int(_id):
                return True
    return False

# ввод ID
def input_id(json_dict: dict):
    while True:
        id_number = input ("Введите ID номер: ")
        if not id_number.isdigit():
            print (" >>> Требуется ввести целое число. Введите ID повторно...")
        elif check_ID (json_dict, int (id_number)):
            print (" >>> Такой ID уже есть в системе. Введите ID повторно...")
        else:
            return id_number

# ввод уровня доступа
def input_access(_min, _max):
    while True:
        access_level = input (f"Введите уровень доступа ({_min}-{_max}): ")
        if not access_level.isdigit():
            print (" >>> Требуется ввести целое число. Введите уровень доступа повторно повторно...")
        elif not (_min <= int(access_level) <= _max):
            print (" >>> Уровень доступа выбран неверно! Введите уровень доступа повторно повторно..")
        else:
            return access_level

# добавления пользователя
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
        save_data_json (json_dict)

# чтение рабочего файла JSON -> передача инфы в словарь: json_dict
def load_data (file_data) -> dict:
    if os.path.exists(file_data):
        with open (file_data, "r", encoding='utf-8') as f:
            json_dict = json.load(f)
    else:
        json_dict = {}
    return json_dict

# запись рабочего файла JSON -> передача инфы из словаря: json_dict
def save_data_json (json_dict):
    with open (file_data, "w", encoding='utf-8') as f:
            json.dump(json_dict, f, indent=4, ensure_ascii=False)
    return

# создание пользоваетелей (экземпляры класса User)
def create_users(_dict: dict):
    users_list = []
    for _lvl, users in _dict.items():
        for _id, _name in users.items():
            users_list.append (User (_name, _id, _lvl))
    return users_list

# ---------- ЗАПУСК ПРОГРАММЫ -------------
dir_path = "E:/codes/Task_13"    # <-- рабочая папка с файлами
file_data = "data_user.json"
init (dir_path)

# json_dict = load_data (file_data)
# users = create_users (json_dict)
# for user in users:
#     print(user)

json_dict = load_data (file_data)
add_user (json_dict)