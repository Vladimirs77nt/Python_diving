# Задание 7

# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. 
# ✔ Каждая группа включает файлы с несколькими расширениями. 
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

# список расширенийб первый элемент - название папки для размещения файлов при сортировке

import os

# папка с файлами / относительно рабочей папки
dir_path = "/Task_07/file_4"

# словаь расширений по группам, ключ - жто название группы и папки назначения
exc_sort = {"_video": ["mp4", "avi", "mov", "mkv"],
            "_image": ["jpg", "tiff", "gif", "png"],
            "_text": ["txt", "doc"],
            }

# папка для "прочих" файлов, с расширениями отличными от тех что есть в словаре
dir_path_other = "_other"

# инициализация папок для сортировки
def init ():
    global dir_path
    default_path = os.getcwd()
    dir_path = default_path + dir_path
    dir_path = dir_path.replace("\\","/")
    try:
        os.chdir(dir_path)
    except:
        os.mkdir(dir_path)
    os.chdir(dir_path)
    list_dir_path = list (exc_sort.keys())
    list_dir_path.append (dir_path_other)
    print (list_dir_path)
    for i in list_dir_path:
        try:
            os.mkdir(i)
        except:
            continue

# основаная функция сорировки файлов
def sort_file_in_dir (_dir):
    os.chdir(_dir)
    for i in os.listdir():      # в циклое проходим по всем фалйам и папкам
        if os.path.isdir(i):    # если это папка - то пропускаем!
                continue
        file_name, file_extension = func_file (i)

        # ищем полученное расширение на соответствие заданному списку
        for type, exc_list in exc_sort.items ():
            if file_extension in exc_list:
                os.replace(i, (f"{type}/{i}"))          # перемещаем в целевую папку
                break
        else:
            os.replace(i, (f"{dir_path_other}/{i}"))    # перемещаем в папку "прочее/other"
    print (f" -- сортировка завершена успешно! --")  

# функция возвращает название файла (до последней точки) и расширение файла
def func_file (file_str):
    *file_name, file_extension = file_str.split(".")
    file_name = ".".join(j for j in file_name)
    return file_name, file_extension

# ---------- ЗАПУСК ПРОГРАММЫ -------------
init ()
sort_file_in_dir (dir_path)