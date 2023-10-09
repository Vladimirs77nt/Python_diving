# Задание №1

# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания (time.time)


from datetime import datetime


class MyString (str):

    def __new__ (cls, value: str, author: str):
        isinstance = super().__new__ (cls, value)
        isinstance.author = author
        isinstance.str_time = datetime.now()
        return isinstance
    
    def __init (self, value: str, author: str):
        pass
        

a = MyString ("Текстовая какая-то строка", "Вова")

print (a, a.author, a.str_time)