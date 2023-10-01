import json
import os


def load_json():
    if os.path.exists(PATH_DB):
        with open(PATH_DB, 'r', encoding='UTF-8') as file:
            data = json.load(file)
    else:
        data = {}
    print (" прочитан ->", data, type (data))
    return data

def input_name():
    return input('Введите имя: ')

def input_id(dict_users: dict):
    list_id = set()
    for users in dict_users.values():
        for user in users:
            for u_id in user:
                list_id.add(u_id)
    while True:
        u_id = input('Введите ID: ')
        if u_id not in list_id and u_id.isdigit():
            return u_id
        print('Такой ID занят, введите заново')

def input_lvl():
    while True:
        lvl = input('Введите уровень доступа: ')
        if lvl.isdigit() and 0 < int(lvl) < 8:
            return lvl

def create_users():
    while True:
        user_db = load_json()
        name = input_name()
        if not name:
            break
        u_id = input_id(user_db)
        lvl = input_lvl()

        if lvl in user_db:
            user_db[lvl].append({u_id: name})
        else:
            user_db[lvl] = [{u_id: name}]
        with open(PATH_DB, 'w', encoding='UTF-8') as file:
            json.dump(user_db, file, indent=4, ensure_ascii=False)


#---------------------------------------
PATH_DB = 'user_db.json'
create_users()