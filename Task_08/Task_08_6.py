# Задание 6

# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import csv
import pickle
import os


# чтение рабочего файла PICKLE -> передача инфы в словарь: data_dict
def load_data_pickle (file_pickle) -> dict:
    with open (file_pickle, "rb") as f:
        data_dict = pickle.load(f)
    print (data_dict)
    return data_dict


# запись рабочего файла CSV -> передача инфы из списка: _result
def save_data_csv (_result, file_csv):
    # кодировку выбираю СПЕЦИАЛЬНО CP1521 - для Excel
    # delimiter=";" - также специально для Excel
    with open (file_csv, "w", encoding='CP1251') as f:
        csv_write = csv.writer(f, dialect="excel", delimiter=";", lineterminator="\n")
        csv_write.writerows(_result)


# запись рабочего файла CSV -> преобразование инфы из словаря: _dict
def convert_pickle_to_csv (file_pickle):
    data_to_convert = load_data_pickle (file_pickle)

    results = []
    for access, users in data_to_convert.items():
        for _id, _items in users.items():
            user = []
            user.append(access)
            user.append(_id)
            user.append(_items[0])
            user.append(_items[1])
            results.append(user)

    results = [[results[j][i] for j in range(len(results))] for i in range(len(results[0]))]
    file_csv = file_pickle.replace(".pickle", ".csv")
    save_data_csv (results, file_csv)

    # with open (file_csv, "w", encoding='utf-8') as f:
    #     csv_write = csv.writer(f, dialect="excel", delimiter="\t", lineterminator="\n")
    #     csv_write.writerows(results)


# ---------- ЗАПУСК ПРОГРАММЫ -------------
dir_path = "E:/codes/Task_08"    # <-- рабочая папка с файлами
os.chdir(dir_path)

file_pickle = "data_user_new.pickle"

convert_pickle_to_csv (file_pickle)