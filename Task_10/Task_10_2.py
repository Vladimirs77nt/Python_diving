# Задание №2

# Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Restangle:

    def __init__(self, length, height=None) -> None:
        self.length = length
        self.height = height if height else length

    def length_r (self):
        return (self.length + self.height)*2
    
    def area_r (self):
        return self.length * self.height
    
restangle_1 = Restangle (20)
print (restangle_1.length_r ())
print (restangle_1.area_r ())