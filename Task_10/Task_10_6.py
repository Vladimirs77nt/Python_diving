# Задание №6

# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.


class Animal:
    def __init__(self, name):
        self.name = name
        self.spec = None

    def show (self):
        return f"{self.name} {self.spec}"
    

class Dog (Animal):
    def __init__(self, name, spec):
        super().__init__(name)
        self.spec = spec
    
class Fish (Animal):
    def __init__(self, name, spec):
        super().__init__(name)
        self.spec = spec
    
class Birds (Animal):
    def __init__(self, name, spec):
        super().__init__(name)
        self.spec = spec


    
Dog_1 = Dog ("Мопс", "гавкает")
print (Dog_1.show ())

Fish_2 = Fish ("Карп", "плавает")
print (Fish_2.show ())

Birds_3 = Birds ("Орел", "летает")
print (Birds_3.show ())