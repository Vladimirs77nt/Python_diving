# ТЕСТ 1.

# Информация об авторе и времени создания

# Разработайте программное обеспечение для ведения журнала событий.
# Вам необходим класс, который будет представлять строки журнала и включать в себя информацию об авторе
# и времени создания каждой записи.

# Создайте класс MyStr, который наследуется от встроенного класса str.
# Этот класс будет представлять строки с информацией о событиях.

# Класс MyStr должен иметь следующие атрибуты:
# * value (str): Строковое значение с описанием события.
# * author (str): Имя автора, создавшего запись.
# * time (float): Время создания записи в формате '%Y-%m-%d %H:%M'.

# Реализуйте метод __new__(cls, value, author),
#   который создает новый объект класса MyStr с заданным value и author.
#   Метод также автоматически фиксирует время создания записи.

# Реализуйте метод __str__(self),
#   который возвращает строковое представление объекта класса MyStr с информацией о событии,
#   авторе и времени создания.

# Реализуйте метод __repr__(self),
#   который возвращает строковое представление объекта класса MyStr для отладки.

from datetime import datetime

class MyStr (str):

    def __new__ (cls, value: str, author: str):
        isinstance = super().__new__ (cls, value)
        return isinstance
    
    def __init__ (self, value: str, author: str):
        self.value = value
        self.author = author
        self.str_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def __str__ (self):
        return f"{self.value} (Автор: {self.author}, Время создания: {self.str_time})"
    
    def __repr__(self):
        return f"MyStr({repr (self.value)}, {repr (self.author)})"


my_string = MyStr("Пример текста", "Иван")
print(my_string)

my_string = MyStr("Другой текст", "Бунин")
print(my_string)

my_string = MyStr("Мама мыла раму", "Маршак")
print(repr(my_string))

my_string = MyStr("Заключительный текст", "Достоевский")
print(repr(my_string))