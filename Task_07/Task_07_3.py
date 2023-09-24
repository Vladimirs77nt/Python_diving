# Задание 3

# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# - если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# - если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле. 
# При достижении конца более короткого файла, возвращайтесь в его начало.

import os
os.chdir("Task_07")     # <-- рабочая папка с файлами

# функция чтения списка из указанного текстового файла
def load_file (file):
    list_file = []
    with open(file, "r", encoding="utf-8") as f:
        for str in list(f):
            list_file.append (str[:-2])
    print (f" -- файл {file} прочитан --")  
    return list_file

# функция записи списка в указанный тексовый файл
def save_to_file (file, list_):
    with open(file, "w", encoding="utf-8") as f:
        for line in list_:
            f.write (line+"\n")
    print (f" -- файл {file} записан --")  

# функция создания списка результата обработки двух входящих файлов
def func_multi_name (file_number, file_name):
    list_num = load_file (file_number)
    list_name = load_file (file_name)
    size_max = len(list_num) if len(list_num) > len(list_name) else len(list_name)
    count_num = 0
    count_name = 0
    list_result = []
    for i in range (size_max):
        if count_num == len (list_num):
            count_num = 0
        if count_name == len (list_name):
            count_name = 0
        num_1, num_2 = list (list_num[count_num].split(" | "))
        name = list_name[count_name]
        multi = int(num_1) * float(num_2)
        if multi < 0:
            str = (f"{name.lower()} {-multi}")
        else:
            str = (f"{name.upper()} {int(multi)}")
        list_result.append (str)
        count_name += 1
        count_num += 1
    print (" -- данные обработаны --")
    print (" << программа завершенна >>")
    return list_result


# ---------- ЗАПУСК ПРОГРАММЫ -------------
file_number = "Task_07_1_number.txt"
file_name =   "Task_07_2_name.txt"
file_result = "Task_07_3_muli_name.txt"

a = func_multi_name (file_number, file_name)
save_to_file (file_result, a)