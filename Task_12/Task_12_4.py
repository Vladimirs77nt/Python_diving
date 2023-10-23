# Задание №4

# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника
# и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

class Rectangle:
  
    def __init__(self, width:float, height:float=None):
        self._width = width
        self._height = height if height else width
        if self._width<=0 or self._height<=0:
            raise ValueError(f"Задано нулевое или отрицательное значение стороны")
        
    @property
    def width(self):
        return self._width
        
    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError(f'Сторона прямоугольника должна быть больше нуля!')
    
    # возвращает информациюо сторонах прямоугольника
    def get_sides (self):
        return (self._width, self._height)
    
    # возвразает текстовое описание типа прямоугольника
    def get_type (self):
        if self._width == self._height:
            return "Квадрат"
        return "Прямоугольник"
    
    # возвращает периметр
    def perimeter (self):
        return (self._width + self._height)*2
    
    # возвращает площадь
    def area (self):
        return self._width * self._height
    
    def __add__ (self, other):
        if isinstance (other, Rectangle):
            return Rectangle (self._width + other._width, float(self._height + other._height))
        raise TypeError
    
    def __str__ (self):
        return f"Прямоугольник со сторонами {self._width} и {self._height}"
    
    def __repr__(self):
        return f"Rectangle({repr (self._width)}, {repr (self._height)})"
    

rect1 = Rectangle (4, 44)
# rect1.width = 10
print (rect1)