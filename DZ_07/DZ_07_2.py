# Задание №2.

# Напишите функцию группового переименования файлов.
# Она должна:
#  - принимать параметр желаемое конечное имя файлов. при переименовании в конце имени добавляется порядковый номер.
#  - принимать параметр количество цифр в порядковом номере.
#  - принимать параметр расширение исходного файла.
#     Переименование должно работать только для этих файлов внутри каталога.
#  - принимать параметр расширение конечного файла.
#  - принимать диапазон сохраняемого оригинального имени.
#     Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
#     К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os
import sys

# инициализация рабочей папки
def init (_dir):
    default_path = os.getcwd()
    dir_path_full = default_path + _dir
    dir_path_full = dir_path_full.replace("\\","/")
    try:
        os.chdir(dir_path_full)
    except:
        dir_path_full = dir_path_full.replace("/","\\")
        sys.exit(f"\n -- Рабочей папки {dir_path_full} не существует. Программа остановлена --\n")

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
    
    print (f" >> Работаем в папке: {os.getcwd()}")

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


# ---------- ЗАПУСК ПРОГРАММЫ -------------
dir_path = "/DZ_07/files"   # <-- рабочая папка с файлами
init (dir_path)             # <--- инициализация рабочей папки

# запуск функции сортировки файлов в рабочей папке
rename_group ("doc", "wrd", [0,5], 4, "_word_file_")