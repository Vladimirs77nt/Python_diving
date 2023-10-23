# 📌 ЗАДАЧА

# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень)
# Напишите 3-7 тестов pytest (или unittest на ваш выбор) для данного проекта
# ОБЯЗАТЕЛЬНО! Используйте фикстуры

    # Задача №5 с семинара 13
    # Доработаем задачи 3 и 4.
    # Создайте класс проекта, который имеет следующие методы:
    # 📌 1) Загрузка данных (функция из задания 4)
    # 📌 2) Вход в систему - требует указать имя и id пользователя
    #     Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство
    #     пользователей. Если такого пользователя нет, вызывайте исключение доступа.
    #     А если пользователь есть, получите его уровень из множества пользователей
    # 📌 3) Добавление пользователя
    #     Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.


import unittest
import json
import os


class TestCaseName(unittest.TestCase):

    # создание фикстур
    def setUp(self) -> None:
        self.user_1 = "Оля", 622                # пользователь с уровнем доступа 4
        self.user_2 = "Джейсон", 7              # несуществующий пользователь
        self.user_3 = "Елена", 223, 5           # пользователь с уровнем доступа 5 (его добавят, потом удалят)
        self.user_4 = "Стоун Семнадцатый", 632  # пользователь с уровнем доступа 7

    # авторизация записанного пользователя из словаря/базы с уровнем 4
    def test_method_1 (self):
        self.assertEqual(Session(*self.user_1).__str__(), ">>> Сессия запущена для пользовтеля Оля c id: 622, уровень доступа: 4")
    
    # попытка авторизации пользователя, которого нет в базе
    def test_method_2 (self):
        self.assertRaises(AccessError, Session, self.user_2)

    # попытка добавления нового пользователя с уровнем (5) выше чем у авторизованного (4)
    def test_method_3 (self):
        self.assertRaises(AccessError, Session(*self.user_1).add_user, *self.user_3)

    # авторизация записанного пользователя из словаря/базы с уровнем 7
    def test_method_4 (self):
        self.assertEqual(Session(*self.user_4).__str__(), ">>> Сессия запущена для пользовтеля Стоун Семнадцатый c id: 632, уровень доступа: 7")

    # добавление нового пользователя с уровнем ниже (5) чем у авторизованного (7) - ожидаем выполнение
    def test_method_5 (self):
        self.assertEqual(Session(*self.user_4).add_user(*self.user_3), ">>> Новый пользователь Елена c id: 223 и уровнем допуска: 5  - добавлен")

    # попытка удаления пользователя с уровнем (5) выше чем у авторизованного (4) - ожидаем ошибку доступа
    def test_method_6 (self):
        self.assertRaises(AccessError, Session(*self.user_1).delete_user, *self.user_3)

    # удаление пользователя с уровнем (5) ниже чем у авторизованного (7) - ожидаем выполнение
    def test_method_7 (self):
        self.assertEqual(Session(*self.user_4).delete_user(*self.user_3), ">>> Пользователь Елена c id: 223 и уровнем допуска: 5  - удален")


# класс ошибки ДОСТУПА
class AccessError (Exception):
    def __init__(self, *args) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None


# класс ПРОЕКТА-СЕССИИ
class Session:

    def __init__(self, user_name=None, user_id=None):

        self.__class__.users_dict = self.load_data()

        # если ИМЯ и ID - явно указаны
        if user_name: 
            self.user_name = user_name
            self.user_id = user_id
        
        # если ИМЯ и ID - НЕ указаны
        else:
            self.user_name, self.user_id, self.level = self.access_to_user(self.__class__.users_dict)
            self.user_id, self.level = int(self.user_id), int(self.level)

        self.user = self.authorization (self.user_id, self.user_name)

        if self.user:
            self.name = self.user.name
            self.id_user = self.user.id_user
            self.access_level = self.user.access_level

        else:
            raise AccessError ("Доступ отказан!")
    
    # АВТОРИЗАЦИЯ (создание пользователя класса User) с пред.проверкой ID пользователя
    def authorization(self, user_id, user_name):
        for _lvl, users in self.__class__.users_dict.items():
            for _id, _name in users.items():
                if int(_id) == user_id and _name == user_name:
                    return User (_name, _id, _lvl)
        return False
    
    # ВВОД ДАННЫХ С ТЕРМИНАЛА ДЛЯ ВХОДА В СИСТЕМУ
    def access_to_user (self, json_dict: dict):
        while True:
            name = input ("Введите имя пользователя: ")
            if not name:
                print (" -- программа завершена --\n")
                break
            id_number, level = self.input_and_check_id(json_dict, name)
            if level:
                return name, id_number, level
            else:
                raise AccessError (f"> Пользователя {name} c id: {id_number} - в базе нет")
        
    # ввод ID с доп.проверкой по имени в базе/словаре
    def input_and_check_id(self, json_dict: dict, name):
        while True:
            id_number = input ("Введите ID номер: ")
            if not id_number.isdigit():
                print ("> Требуется ввести целое число. Введите ID повторно...")
            else:
                for _level, users in json_dict.items():
                    for _id, _name in users.items():
                        if int(id_number) == int(_id) and name == _name:
                            return id_number, _level
                print (" --- в базе НЕТ пользователя с таким именем и ID номером ---")
            return id_number, None
        
    # проверка ID в базе
    def check_ID (self, json_dict: dict, num_id: int):
        for users in json_dict.values():
            for _id in users.keys():
                if int(num_id) == int(_id):
                    return True
        return False
    
    # добавление нового пользователя (класс User)
    def add_user (self, user_name, user_id, user_level):
        if user_level>int(self.user.access_level):
            raise AccessError ("Ваш уровень допуска не позволяет добавлять нового пользователя!")
        if not self.check_ID (self.__class__.users_dict, str(user_id)):
            if str(user_level) in self.__class__.users_dict.keys():
                self.__class__.users_dict[str(user_level)][str(user_id)] = user_name
            else:
                self.__class__.users_dict[str(user_level)] = {str(user_id): user_name}
            self.save_data_json (self.__class__.users_dict, file_path)
            result = (f">>> Новый пользователь {user_name} c id: {user_id} и уровнем допуска: {user_level}  - добавлен")
            print (result)
            return result
        else:
            raise Exception (f"Пользователь {self.name} с таким ID ({self.id_user}) уже есть в системе")
    
    # удаление поььзователя
    def delete_user (self, user_name, user_id, user_level):
        if user_level>int(self.user.access_level):
            raise AccessError (f"Ваш уровень допуска не позволяет удалять пользователя с уровнем {user_level}!")
        if self.check_ID (self.__class__.users_dict, str(user_id)):
            del self.__class__.users_dict[str(user_level)][str(user_id)]
            self.save_data_json (self.__class__.users_dict, file_path)
            result = (f">>> Пользователь {user_name} c id: {user_id} и уровнем допуска: {user_level}  - удален")
            print (result)
            return result
        else:
            raise Exception (f"Пользователя {self.name} с ID ({self.id_user}) нет в системе")
    
    # функция чтения рабочего файла JSON -> передача инфы в словарь: json_dict
    def load_data (self) -> dict:
        if os.path.exists(file_path):
            with open (file_path, "r", encoding='utf-8') as f:
                json_dict = json.load(f)
        else:
            json_dict = {}
        return json_dict
    
    # запись рабочего файла JSON -> передача инфы из словаря: json_dict
    def save_data_json (self, json_dict, file_path):
        with open (file_path, "w", encoding='utf-8') as f:
            json.dump(json_dict, f, indent=4, ensure_ascii=False)
        return True
    
    def __str__(self) -> str:
        return f">>> Сессия запущена для пользовтеля {self.name} c id: {self.id_user}, уровень доступа: {self.access_level}"


# КЛАСС пользователя User
class User:

    def __init__(self, name, id_user, access_level):
        self.name = name
        self.id_user = id_user
        self.access_level = access_level

    def __str__ (self):
        return f"Пользователь {self.name}, ID: {self.id_user}, уровень доступа: {self.access_level}"
    
    def __eq__(self, other: object) -> bool:
        return self.id_user == other.id_user    


# ---------- ЗАПУСК ПРОГРАММЫ ----------------------------------- 
dir_path = "E:/codes/DZ_14"    # <-- рабочая папка с файлами
file_path = "data_user.json"

try:
    os.chdir(dir_path)
except:
    os.mkdir(dir_path)
    os.chdir(dir_path)


unittest.main(verbosity=2)

# user = "Оля", 622
# my_session = Session (*user)
# print(my_session)
# my_session.add_user (