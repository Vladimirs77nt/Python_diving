# Задание 7

# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.

import pickle
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

# чтение рабочего файла CSV -> передача инфы в список
def convert_csv_to_pickle (file_csv):
    result = []
    with open (file_csv, "r", encoding='CP1251') as f:
        csv_data = csv.reader (f, dialect="excel", delimiter=";")
        for i in csv_data:
            result.append (i)
    print ("\ncsv строка:")
    print (result)

    # из csv списка делаем pickle строку с помощью pickle.dumps
    res = pickle.dumps(result,protocol=pickle.DEFAULT_PROTOCOL)
    print ("\npickle строка:")
    print (res)
    return


# ---------- ЗАПУСК ПРОГРАММЫ -------------
dir_path = "E:/codes/Task_08"    # <-- рабочая папка с файлами
init (dir_path)

file_csv = "data_user_new.csv"

convert_csv_to_pickle (file_csv)