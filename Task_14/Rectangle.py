class Rectangle:

    def __new__(self, width: float, height: float=None):
        isinstance = super().__new__ (self)
        return isinstance
    
    def __init__(self, width: float, height: float=None):
        self.width = width
        self.height = height if height else width
        if self.width<=0 or self.height<=0:
            raise ValueError(f"Задано нулевое или отрицательное значение стороны")
    
    # тип
    def get_type (self):
        if self.width == self.height:
            return "Квадрат"
        return "Прямоугольник"
    
    # периметр
    def perimeter (self):
        return (self.width + self.height)*2
    
    # площадь
    def area (self):
        return self.width * self.height
    
    # сложение
    def __add__ (self, other):
        if isinstance (other, Rectangle):
            return Rectangle (self.width + other.width, float(self.height + other.height))
        raise TypeError
    
    # вычитание
    def __sub__ (self, other):
        if isinstance (other, Rectangle):
            c = self.width - other.width
            d = float(self.height - other.height)
            if c <= 0 or d <= 0:
                raise ValueError(f"Результат вычитания отрицателный!")
            return Rectangle (c, d)
        raise TypeError
    
    # равно =
    def __eq__ (self, other):
        return self.area() == other.area()
    
    # меньше <
    def __lt__ (self, other):
        return self.area() < other.area()
    
    # меньше или равно <=
    def __ge__ (self, other):
        return self.area() >= other.area()
    
    def __str__ (self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}" if self.width != self.height else f"Квадрат со стороной {self.width}"
    
    def __repr__(self):
        return f"Rectangle({repr (self.width)}, {repr (self.height)})"