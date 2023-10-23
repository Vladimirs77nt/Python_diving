# ТЕСТ 2.

# Класс Archive - архив текстовых и числовых записей

# Класс Archive - архив текстовых и числовых записей

# Разработайте программу для хранения и управления текстовыми и числовыми записями.
# Вам нужно создать класс Archive, который будет представлять архив и реализовывать следующую функциональность:

# Класс Archive должен иметь следующие атрибуты:

# archive_text (list): Список архивированных текстовых записей.
# archive_number (list): Список архивированных числовых записей.
# text (str): Текущая текстовая запись, которую нужно добавить в архив.
# number (int или float): Текущая числовая запись, которую нужно добавить в архив.
# Класс Archive должен реализовать шаблон Singleton, чтобы гарантировать, что существует только один экземпляр архива.
# Класс Archive должен иметь метод __init__(self, text: str, number: int | float), который принимает текстовую
# и числовую запись и сохраняет их как текущие записи для добавления в архив.

# Класс Archive должен реализовать методы
# __str__(self) и __repr__(self), чтобы можно было получить строковое представление текущих записей и архива.


# Пример

# На входе:

# archive1 = Archive("Запись 1", 42)
# archive2 = Archive("Запись 2", 3.14)


# На выходе:

# Text is Запись 1 and number is 42. Also ['Запись 1'] and [42]
# Text is Запись 2 and number is 3.14. Also ['Запись 1', 'Запись 2'] and [42, 3.14]


import copy

class Archive:
    archive_text = []
    archive_number = []
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self,  text: str, number: [int, float]):
        self.number = number
        self.text = text
        self.archive_text = copy.deepcopy(Archive.archive_text)
        self.archive_number = copy.deepcopy(Archive.archive_number)
        Archive.archive_text.append (text)
        Archive.archive_number.append (number)

    def __str__ (self):
        return f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"
    
    def __repr__(self):
        return f"Archive({repr (self.text)}, {repr (self.number)})"
    


archive1 = Archive("First Text", 1)
print(archive1)
archive2 = Archive("Second Text", 2)
print(archive2)
archive3 = Archive("Third Text", 3)
print(archive1)
print(archive3)