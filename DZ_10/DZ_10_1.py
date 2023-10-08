# Задание

# 1. Решить задания, которые не успели решить на семинаре.
# 2. Доработаем задания 5-6. Создайте класс-фабрику:
#     Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
#     Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# 3. Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
#     Превратите функции в методы класса, а параметры в свойства.
#     Задания должны решаться через вызов методов экземпляра.

# КЛАСС-ФАБРИКА ЖИВОТНЫХ


from random import choice as rnd_choice


# родительский класс животных
class Animal:

    # метод создания нового животного
    def create_animal (animal_type, name, spec=None):
        match animal_type:
            case "dog":
                return Dog(name, spec)
            case "cat":
                return Cat(name, spec)
            case "fish":
                return Fish(name, spec)
            case "bird":
                return Bird(name, spec)
            case _:
                raise ValueError ("such an animal does not exist in the list")

    # функция инициализации параметров нового животного
    def __init__(self, name):
        self.name = name
        self.spec = None
         
    def show_animal (self):
        return f"{self.get_type()} {self.name}: {self.spec}"
    

class Dog (Animal):
    def __init__(self, name, spec):
        super().__init__(name)
        self.name = name
        self.spec = spec if spec else "гав-гав!"
        
    def get_type (self):
        return "собака"
    

class Cat (Animal):
    def __init__(self, name, spec):
        super().__init__(name)
        self.name = name
        self.spec = spec if spec else "мур-мур!"
        
    def get_type (self):
        return "кошка"


class Fish (Animal):
    def __init__(self, name, spec):
        super().__init__(name)
        self.name = name
        self.spec = spec if spec else "плавает"
        
    def get_type (self):
        return "рыба"


class Bird (Animal):
    def __init__(self, name, spec):
        super().__init__(name)
        self.name = name
        self.spec = spec if spec else "летает"
        
    def get_type (self):
        return "птица"



# ------------------ БЛОК ЗАПУСКА ---------------------

name_list = ["Мухтар", "Бим", "Валет", "Секунда", "Гульсары", "Бим", "Руслан", "Багира", "Друг", "Егорка", "Митька",
             "Брут", "Матроскин", "Гав", "Музгарка", "Артемон", "Гоша", "Крепыш", "Лобо", "Лома", "Арто", "Лютый",
             "Миш-Миш", "Непоседа", "Чернушка", "Кубик", "Раздан", "Пятнашка", "Солли", "Мустанг", "Вулкан",
             "Зарница", "Доня", "Микки", "Рыжик", "Алый", "Буран", "Маркиз", "Чанду", "Рару", "Нука", "Рыжая Фея",
             "Кунак", "Сероманец", "Трехлапый", "Малыш", "Тортилла"]

animal_type = ["cat", "dog", "fish", "bird"]

animal_factory = []

print ()
for i in range (10):
    new_animal = Animal.create_animal(rnd_choice(animal_type), rnd_choice(name_list))
    animal_factory.append (new_animal)
    print (f"{i+1}\t{new_animal.show_animal()}")

print ()
print ("Все работает!!!")
print ()

print ("А теперь...")
# специальная проверка животного которого нет в списке!
leon_1 = Animal.create_animal("leon", "Лева", "Рррррр!!!")