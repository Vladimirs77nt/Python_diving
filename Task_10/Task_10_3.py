# Задание №3

# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п.
# на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.


class People:

    def __init__(self, last_name, first_name, patronymic, age):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.__age = age

    def birthday (self):
        self.__age += 1

    def full_name (self):
        return self.last_name + " " + self.first_name + " " + self.patronymic
    
    def show_age (self):
        return self.__age
    
people_1 = People ("Сидоров", "Иван", "Васильевич", 45)
print (people_1.full_name (), people_1._People__age)
people_1.birthday ()
people_1.birthday ()
people_1.birthday ()
print (people_1.full_name (), people_1.show_age())

people_1.first_name = "Сергей"
print (people_1.full_name (), people_1.show_age())

people_1._People__age = 20
print (people_1.full_name (), people_1.show_age())