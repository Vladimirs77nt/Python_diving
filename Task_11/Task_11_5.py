# Задание №5

# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.


class Rectangle:

    def __new__(self, a: float, b: float=None):
        isinstance = super().__new__ (self)
        return isinstance
    
    def __init__(self, a: float, b: float=None):
        self.a = a
        self.b = b if b else a
        if self.a<=0 or self.b<=0:
            raise ValueError(f"Задано нулевое или отрицательное значение стороны")
    
    # возвращает информациюо сторонах прямоугольника
    def get_sides (self):
        return (self.a, self.b)
    
    # возвразает текстовое описание типа прямоугольника
    def get_type (self):
        if self.a == self.b:
            return "Квадрат"
        return "Прямоугольник"
    
    # возвращает периметр
    def perimetr (self):
        return (self.a + self.b)*2
    
    # возвращает площадь
    def area (self):
        return self.a * self.b
    
    def __add__ (self, other):
        if isinstance (other, Rectangle):
            return Rectangle (self.a + other.a, self.b + other.b)
        raise TypeError
    
    def __sub__ (self, other):
        if isinstance (other, Rectangle):
            c = self.a - other.a
            d = self.b - other.b
            if c <= 0 or d <= 0:
                raise ValueError(f"Результат вычитания отрицателный!")
            return Rectangle (c, d)
        raise TypeError
    

a1 = Rectangle (15, 18)
a2 = Rectangle (6, 3)
a3 = "текст"

i = a1 + a2
r = a1 - a2
print (f"сложение: -> {i.get_sides()}, {i.get_type()}, площадь: {i.area()}")
print (f"вычитание: -> {r.get_sides()}, {r.get_type()}, площадь: {r.area()}")