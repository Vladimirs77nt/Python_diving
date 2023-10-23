# Задача №5

# Доработаем задачи 3 и 4.

# Создайте класс проекта, который имеет следующие методы:
# 📌 загрузка данных (функция из задания 4)
# 📌 вход в систему - требует указать имя и id пользователя
#     Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей
#     Если такого пользователя нет, вызывайте исключение доступа.
#     А если пользователь есть, получите его уровень из множества пользователей
# 📌 добавление пользователя
#     eсли уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.


import json
import os


# класс сессии
class Session:

    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.__class__.users_dict = self.load_data()
        self.user = self.authorization (user_id, user_name)
        if self.user:
            self.name = self.user.name
            self.id_user = self.user.id_user
            self.access_level = self.user.access_level
            print (f"Пользовтель {self.name} c ID: {self.id_user} - авторизован !!!")

        else:
            raise Exception ("Доступ отказан!")

    # чтение рабочего файла JSON -> передача инфы в словарь: json_dict
    def load_data (self) -> dict:
        if os.path.exists(file_path):
            with open (file_path, "r", encoding='utf-8') as f:
                json_dict = json.load(f)
        else:
            json_dict = {}
        return json_dict
    
    def authorization(self, id_user, name_user):
        for _lvl, users in self.__class__.users_dict.items():
            for _id, _name in users.items():
                if int(_id) == id_user and _name == name_user:
                    return User (_name, _id, _lvl)
        return False
    
    def add_user (self, user_name, user_id, user_level):
        if user_level>int(self.user.access_level):
            raise Exception ("Ваш уровень допуска не позволяет добавить нового пользователя!")
        if not check_ID (self.__class__.users_dict, str(user_id)):
            if str(user_level) in self.__class__.users_dict.keys():
                self.__class__.users_dict[str(user_level)][str(user_id)] = user_name
            else:
                self.__class__.users_dict[str(user_level)] = {str(user_id): user_name}
            save_data_json (self.__class__.users_dict)
            print (" -- новый пользователь добавлен! --")
        else:
            raise Exception ("Пользователь с таким ID уже есть в системе")
    
    def __str__(self) -> str:
        return f" << сессия пользовтеля {self.name} c id: {self.id_user}, уровень доступа: {self.access_level} >>"


# класс пользователя
class User:

    def __init__(self, name, id_user, access_level):
        self.name = name
        self.id_user = id_user
        self.access_level = access_level

    def __str__ (self):
        return f"Пользователь {self.name}, ID: {self.id_user}, уровень доступа: {self.access_level}"
    
    def __eq__(self, other: object) -> bool:
        return self.id_user == other.id_user


# --------------------------------------------------------------
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
def load_data () -> dict:
    if os.path.exists(file_path):
        with open (file_path, "r", encoding='utf-8') as f:
            json_dict = json.load(f)
    else:
        json_dict = {}
    return json_dict

# запись рабочего файла JSON -> передача инфы из словаря: json_dict
def save_data_json (json_dict):
    with open (file_path, "w", encoding='utf-8') as f:
            json.dump(json_dict, f, indent=4, ensure_ascii=False)
    return


# ---------- ЗАПУСК ПРОГРАММЫ -------------
dir_path = "E:/codes/Task_13"    # <-- рабочая папка с файлами
file_path = "data_user.json"
init (dir_path)

my_session = Session ("Игорь", 326)
print (my_session)

my_session.add_user ("Мирон", 322, 7)