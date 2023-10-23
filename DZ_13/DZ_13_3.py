# ТЕСТ №3

# Управление информацией о сотрудниках и их возрасте

# В организации есть два типа людей: сотрудники и обычные люди.

# Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
#  - Фамилия (строка, не пустая)
#  - Имя (строка, не пустая)
#  - Отчество (строка, не пустая)
#  - Возраст (целое положительное число)

# Сотрудники имеют также уникальный идентификационный номер (ID),
# который должен быть шестизначным положительным целым числом.

# Ваша задача:

# 1) Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях
#    (Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и генерировать
#     исключения InvalidNameError и InvalidAgeError, если данные неверные.

# 2) Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер ID.
#    Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.

# 3) Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.

# 4) Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр
#    в его ID (по остатку от деления на 7).

# 5) Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают
#    корректно при передаче неверных данных.

# класс ошибки ИМЕНИ
class InvalidNameError (Exception):
    def __init__(self, *args) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None


# класс ошибки ВОЗРАСТА
class InvalidAgeError (Exception):
    def __init__(self, *args) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None


# класс ощибки ID номера
class InvalidIdError (Exception):
    def __init__(self, *args) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None


class Person:

    def __init__(self, surname, name, patronymic, age):
        self.surname = surname  # Фамилия
        self.name = name        # Имя
        self.patronymic = patronymic # Отчество
        self.age = age          # Возраст

    def birthday (self):
        self.age = self.age + 1

    def get_age (self):
        return self.age
    

class Employee (Person):

    id_list = []

    def __init__(self, surname, name, patronymic, age, id_employee):
        super().__init__(surname, name, patronymic, age)
        if self.check_name(surname):
            self.surname = surname
        if self.check_name(name):
            self.name = name
        if self.check_name(patronymic):
            self.patronymic = patronymic
        if self.check_age(age):
            self.age = age
        if self.check_id(id_employee):
            self.id_employee = id_employee
            Employee.id_list.append (id_employee)


    def check_name (self, name_check):
        if not isinstance(name_check, str) or name_check == "":
            raise InvalidAgeError (f"Ошибка имени!")
        return True
    
    def check_age (self, age_check):
        if not isinstance(age_check, int) or age_check<0:
            raise InvalidNameError (f"Ошибка возраста!")
        return True
    
    def check_id (self, id_check):
        if not isinstance (id_check, int) or not (0 < id_check < 999999):
            raise InvalidIdError (f"Ошибка ID !!!")
        for i in Employee.id_list:
            if i == id_check:
                raise InvalidIdError (f"Работник с таким ID уже есть!")
        return True

    def get_level (self):
        digits = str(self.id_employee)
        sum = 0
        for digit in digits:
            sum += int(digit)
        return sum%7
    
    def __str__ (self):
        return f"Пользователь {self.surname} {self.name} {self.patronymic}, id: {self.id_employee}, возраст: {self.age}"    
    

user1 = Employee ("Иванов", "Иван", "Иванович", 29, 123)
user2 = Employee ("Иванов", "Иван", "Иванович", 10, 5)
print (user2)
user2.birthday ()
print (user2)

print (user2.get_level())



person = Person("Alice", "Smith", "Johnson", 25)
print(person.get_age())