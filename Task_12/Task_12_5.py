# Задание №5

# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.


class Rectangle:

    __slots__ = ["_width", "_height"]
   
    def __init__(self, width:float, height:float=None):
        self._width = width
        self._height = height if height else width
        
    @property
    def width(self):
        return self._width
        
    @width.setter
    def width(self, value):
        self._width = value
    
    # возвразает текстовое описание типа прямоугольника
    def get_type (self):
        if self._width == self._height:
            return "Квадрат"
        return "Прямоугольник"
    
    def __str__ (self):
        return f"{self.get_type()} со сторонами {self._width} и {self._height}"


rect1 = Rectangle (4, 4)
# rect1.width = 10
print (rect1)
# rect1.color = "green"