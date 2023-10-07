# Задание №5

# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.


class Dog:
    def __init__(self, name, age, wool):
        self.name = name
        self.age = age
        self.wool = wool        # шерсть 

    def show (self):
        return f"Собака {self.name}, {self.wool}"
    
class Fish:
    def __init__(self, name, age, river_fish):
        self.name = name
        self.age = age
        self.river_fish = river_fish    # речная или морская 

    def show (self):
        return f"Рыба {self.name}, {self.river_fish}"
    
class Birds:
    def __init__(self, name, age, flight):
        self.name = name
        self.age = age
        self.flight = flight    # перелетная 

    def show (self):
        return f"Птица {self.name}, {self.flight}"
    
Dog_1 = Dog ("Мопс", 3, "гладкошерстный")
print (Dog_1.show ())

Fish_2 = Fish ("Карп", 2, "речная")
print (Fish_2.show ())

Birds_3 = Birds ("Орел", 1, "не переолетный")
print (Birds_3.show ())