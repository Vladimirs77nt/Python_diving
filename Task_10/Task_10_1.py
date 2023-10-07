# Задание №1

# Создайте класс окружность. Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

from math import pi

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def length_c (self):
        return self.radius*2*pi
    
    def area_c (self):
        return pi*self.radius**2
    

circle_1 = Circle (10)
print (circle_1.length_c())
print (circle_1.area_c ())

circle_2 = Circle (1)
print (circle_2.length_c())
print (circle_2.area_c ())