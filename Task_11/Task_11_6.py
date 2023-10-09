# Задание №6

# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

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
    
    # равно =
    def __eq__ (self, other):
        return self.area () == other.area ()
    
    # НЕ равно !=
    def __ne__ (self, other):
        return self.area () != other.area ()
    
    # больше >
    def __gt__ (self, other):
        return self.area () > other.area ()
    
    # меньше или равно <=
    def __ge__ (self, other):
        return self.area () <= other.area ()
    

a1 = Rectangle (4, 4)
a2 = Rectangle (2, 8)

print (f"{a1}, {a2}")
print (f"равно: = {a1==a2}")
print (f"не равно: = {a1!=a2}")
print (f"больше: > {a1>a2}")
print (f"меньше: < {a1<a2}")
print (f"меньше или равно: <= {a1<=a2}")
print (f"больше или равно: >= {a1>=a2}")