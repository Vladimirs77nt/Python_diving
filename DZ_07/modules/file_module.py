# МОДУЛЬ ДЛЯ РАБОТЫ С ФАЙЛАМИ

import os
import random
import string

SIZE_NAME_MIN = 6
SIZE_NAME_MAX = 30
SIZE_BYTE_MIN = 256
SIZE_BYTE_MAX = 4096
COUNT_FILE = 42

LETTERS = string.ascii_lowercase

# словаь расширений по группам, ключ - жто название группы и папки назначения
exc_sort = {"_video": ["mp4", "avi", "mov", "mkv"],
            "_image": ["jpg", "tiff", "gif", "png"],
            "_text": ["txt", "doc"],
            }

# папка для "прочих" файлов, с расширениями отличными от тех что есть в словаре
dir_path_other = "_other"

# инициализация рабочей папки
def init (_dir):
    default_path = os.getcwd()
    dir_path_full = default_path + _dir
    dir_path_full = dir_path_full.replace("\\","/")
    try:
        os.chdir(dir_path_full)
    except:
        os.mkdir(dir_path_full)
        os.chdir(dir_path_full)

# инициализация папок для сортировки
def init_sort_folder (_dir):
    default_path = os.getcwd()
    dir_path = default_path + _dir
    dir_path = dir_path.replace("\\","/")
    try:
        os.chdir(dir_path)
    except:
        os.mkdir(dir_path)
        os.chdir(dir_path)
    list_dir_path = list (exc_sort.keys())
    for i in list_dir_path:
        try:
            os.mkdir(i)
            print (f" -- папка {i} для файлов типа {str(exc_sort[i])} создана!")
        except:
            continue

# --- функция возвращает название файла (до последней точки) и расширение файла (кортеж) ---
# file_str          - строковое название файла с расширением
def file_get_name_extesion (file_str):
    *file_name, file_extension = file_str.split(".")
    file_name = ".".join(j for j in file_name)
    return file_name, file_extension

# --- функция группового переименования файлов ---
# (1) _exc_file_in      - расширение файлов до переименования (искомое)
# (2) _exc_file_out     - расширение файлов после переимнования
# (3) _origin_name_range: [int, int] - диапазон сохраняемых букв от исходного имени, последняя цифра не включительно!
# (4) _digit            - кол-во цифр в порядковом номере
# (5) _file_name_out    - желаемое имя переименованных файлов (не обязательный аргумент)
# ---> возвращает кол-во переименованных файлов
def rename_group (_exc_file_in: str, _exc_file_out: str, _origin_name_range: [int, int], _digit: int,
                  _file_name_out=""):    
    init ("/files" ) # инициализация рабочей папки
    print (f" >> Работаем в каталоге: {os.getcwd()}")

    count = 0       # порядковый номер файла
    for i in os.listdir():      # в циклое проходим по всем фалйам и папкам
        if os.path.isdir(i):    # если это папка - то пропускаем!
                continue
        file_name, file_extension = file_get_name_extesion (i)
        # сравниваем полученное расширение на соответствие заданному ()
        if file_extension == _exc_file_in:
            new_name = file_name[_origin_name_range[0]: _origin_name_range[1]] + _file_name_out + (f"{count:0{_digit}}") + "." + _exc_file_out
            os.rename (i, new_name)
            print (f" -- файл: {i:.<45} переименовывается -->  {new_name}")
            count += 1
    if count == 0:
         print (f" >> файлы с расширением {_exc_file_in} не найдены\n")
    else:
         print (f" >> Обработка файлов завершена. Переименовано {count} файлов\n")
    return count

# функция генерирует случайное имя:
# SIZE_NAME_MIN - минимальное кол-во букв в имени
# SIZE_NAME_MAX - максимальнео кол-во букв в имени
def generate_name ():
    size = random.randint (SIZE_NAME_MIN, SIZE_NAME_MAX)
    name = ""
    for i in range (size):
        name += random.choices(list(LETTERS))[0]
    name = "".join (name)
    return name

# функция генерирует файлы со случайным именем, с заданным расширением и кол-вом
def generaor_file (file_exp, count=COUNT_FILE):
    for i in range(count):
        file_name = (f"{i}_{generate_name()}.{file_exp}")
        with open(file_name, "w", encoding="utf-8") as f:
            f.write (str(random.randint(0, 1_000_000)))
            print (f" -- файл {file_name} записан --")

# функция генерирует файлы по входящим расширениям с указанием кол-ва файлов
# первым аргументом указывается рабочая папка !!!
def generaor_file_many (_dir, **kwargs):
    try:
        os.chdir(_dir)
    except:
        os.mkdir(_dir)

    os.chdir(_dir)
    for file_exp, count in kwargs.items():
        generaor_file (file_exp, count)


# функция сортировки файлов
def sort_file_in_dir (_dir):
    init_sort_folder (_dir)
    count = 0
    for i in os.listdir():      # в циклое проходим по всем фалйам и папкам
        if os.path.isdir(i):    # если это папка - то пропускаем!
                continue
        file_name, file_extension = func_file (i)

        # ищем полученное расширение на соответствие заданному списку
        for type, exc_list in exc_sort.items ():
            if file_extension in exc_list:
                os.replace(i, (f"{type}/{i}"))          # перемещаем в целевую папку
                count += 1
                break
    if count > 0:
        print (f" -- сортировка завершена успешно! Отсортировано {count} файлов --\n")
    else:
        print (" -- файлов для сортировки не найдено --\n")
    return count