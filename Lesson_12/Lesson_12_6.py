# 6. Экономим память


from math import sqrt

class Triangle:

    __slots__ = ('_a', '_b', '_c')

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self._a}, {self._b}, {self._c}'
    
    def __repr__(self):
        return f'Triangle({self._a}, {self._b}, {self._c})'
    
    def __eq__(self, other):
        first = sorted((self._a, self._b, self._c))
        second = sorted((other._a, other._b, other._c))
        return first == second
    
    def area(self):
        p = (self._a + self._b + self._c) / 2
        _area = sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
        return _area
    
    def __lt__(self, other):
        return self.area() < other.area()
    
    def __hash__(self):
        return hash((self._a, self._b, self._c))
    
triangle = Triangle(3, 4, 5)
print(triangle)
print(triangle.__dict__)
print(Triangle.__dict__)