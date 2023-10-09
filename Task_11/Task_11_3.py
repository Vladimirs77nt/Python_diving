# Задание №3

# Добавьте к задачам 1 и 2 строки документации для классов.

import copy
from datetime import datetime


class MyString (str):
    """Класс MyString - добавляет информацию об авторе и дате/времени создания строки"""

    def __new__ (cls, value: str, author: str):
        isinstance = super().__new__ (cls, value)
        isinstance.author = author
        isinstance.str_time = datetime.now()
        return isinstance
    

class Archive:
    """Класс архивирует пару значений в переменной класса <Archive.archive_list>"""
    archive_list = []
    
    def __init__(self,  num: int, text: str):
        self.num = num
        self.text = text
        self.archive = copy.deepcopy(Archive.archive_list)
        Archive.archive_list.append ([num, text])
    

# ------------------ БЛОК ЗАПУСКА ---------------------

a = MyString ("Текстовая какая-то строка", "Вова")
print (a, a.author, a.str_time)

a1 = Archive (10, "Вова")
a2 = Archive (20, "Люба")
a3 = Archive (25, "Анжелика")
print (a1.num, a1.text, a1.archive)
print (a2.num, a2.text, a2.archive)
print (a3.num, a3.text, a3.archive)


# help (MyString)
help (Archive)