# Задание №6

# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.


class Validator:

    def __init__(self, min_value: int = None):
        self.min_value = min_value if min_value else 0

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')
    
    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {self.param_name}({value}) должно быть больше {self.min_value}')
        

class Rectangle:

    _width = Validator (0)
    _height = Validator (0)
  
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
    
    

rect1 = Rectangle (4, -2)
# rect1.width = 10
print (rect1)