# Задача 2

# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def func_file_path (file):
    *a, b = file_path.split("\\")               # слитуем по "\" на 2 части: всю "левую" часть до последней "\"" - и далее до конца
    path_file = "\\".join(i for i in a)         # "левую" часть собираем обратно - это полный путь
    # так как бывают нахвания с точками - определяем где последняя точка
    *file_name, file_extension = b.split(".")   # "прааую" часть также сплитуем по точкам на 2 части: всю "левую" часть до последней "."
    file_name = ".".join(j for j in file_name)  # "левую" часть собираем обратно - это полное название без расширения
    print ()
    print (f"            Путь:   {path_file}")
    print (f"       имя файла:   {file_name}")
    print (f"расширение файла:   {file_extension}")
    print ()

file_path = "C:\Program Files\Corel\CorelDRAW Graphics Suite 2020\Draw\GMS\CalendarWizard.gms"
func_file_path (file_path)
