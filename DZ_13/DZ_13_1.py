# ТЕСТ №1

# Исключение NegativeValueError

# Добавьте в задачу Rectangle, которую писали ранее, исключение NegativeValueError, которое выбрасывается
# при некорректных значениях ширины и высоты, как при создании объекта, так и при установке их через сеттеры.


class NegativeValueError (Exception):
    def __init__(self, *args) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return self.message
        else:
            return "NegativeValueError has been raised"
    
class Rectangle:

    def __new__(self, width: float, height: float=None):
        isinstance = super().__new__ (self)
        return isinstance
    
    def __init__(self, width: float, height: float=None):
        self._width = width
        self._height = height if height else width
        if self._width <=0:
           raise NegativeValueError(f"Ширина должна быть положительной, а не {self._width}")
        if self._height <=0:
           raise NegativeValueError(f"Высота должна быть положительной, а не {self._height}")  


    @property
    def width(self):
        return self._width
      
    @width.setter
    def width(self, value):
        if value <=0:
           raise NegativeValueError(f"Ширина должна быть положительной, а не {value}") 
        self._width = value

    @property
    def height(self):
        return self._height
      
    @width.setter
    def height(self, value):
        if value <=0:
           raise NegativeValueError(f"Высота должна быть положительной, а не {value}") 
        self._height = value


    def bar(self):
        print('произошло присвоение')

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
    
    def __sub__ (self, other):
        if isinstance (other, Rectangle):
            c = self._width - other._width
            d = float(self._height - other._height)
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
        return f"Прямоугольник со сторонами {self._width} и {self._height}"
    
    def __repr__(self):
        return f"Rectangle({repr (self._width)}, {repr (self._height)})"


# r = Rectangle(-2)

# r = Rectangle(5, -3)

# r = Rectangle(4, 4)
# r.width = -3

r = Rectangle(4, 4)
r.height = -3