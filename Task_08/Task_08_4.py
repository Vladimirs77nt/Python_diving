# Задание 4

# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями. В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.

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

# чтение рабочего файла CSV -> передача инфы в список
def convert_csv_to_json (file_csv, file_json):
    json_dict = {}
    with open (file_csv, "r", encoding='utf-8') as f:
        csv_data = csv.reader (f, dialect="excel", delimiter="\t")
        for i in csv_data:
            access_level = i[0]
            id_number = i[1].zfill(10)
            name = i[2]
            # name = name.title
            hash_key = hash(id_number + name)
            if access_level in json_dict.keys():
                json_dict[access_level][id_number] = [name, hash_key]
            else:
                json_dict[access_level] = {id_number: [name, hash_key]}
        with open (file_json, "w", encoding='utf-8') as f:
            json.dump(json_dict, f, indent=4, ensure_ascii=False)
    return


# ---------- ЗАПУСК ПРОГРАММЫ -------------
dir_path = "E:/codes/Task_08"    # <-- рабочая папка с файлами
init (dir_path)

file_json = "data_user_new.json"
file_csv = "data_user.csv"

convert_csv_to_json (file_csv, file_json)