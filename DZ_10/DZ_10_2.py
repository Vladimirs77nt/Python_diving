# Задание

# 1. Решить задания, которые не успели решить на семинаре.
# 2. Доработаем задания 5-6. Создайте класс-фабрику:
#     Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
#     Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# 3. Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
#     Превратите функции в методы класса, а параметры в свойства.
#     Задания должны решаться через вызов методов экземпляра.

# КЛАСС ТРЕУГОЛЬНИК


class Triangle:

    def __init__(self, a: float, b: float=None, c: float=None) -> None:
        self.a = a
        self.b = b if b else a
        self.c = c if c else b if b else a
        if not self.check_t():
            raise ValueError(f"Треугольник со сторонами: {self.a}, {self.b}, {self.c} - не может быть создан")
        
    # проверка сторон треугольника
    def check_t (self):
        if self.a<=0 or self.b<=0 or self.c<=0:
            return False
        return (self.a+self.b)>self.c and (self.b+self.c)>self.a and (self.a+self.c)>self.b
    
    # возвращает информациюо сторонах треугольника
    def get_sides (self):
        return (self.a, self.b, self.c)
    
    # возвразает текстовое описание типа треугольника
    def get_type (self):
        # проверка треугольника на равносторонность
        if self.a == self.b == self.c:
            return "Равносторонний"
        type = 0
        # проверка треугольника на прямоугольность
        if ((self.a**2 + self.b**2) == self.c**2) or ((self.a**2 + self.c**2) == self.b**2) or ((self.b**2 + self.c**2) == self.a**2):
            type = 1
        # проверка треугольника на равнобедренность
        if (self.a == self.b) or (self.a == self.c) or (self.b == self.c):
            type += 10
        if type == 1:
            return "Прямоугольный"
        if type == 11:
            return "Прямоугольный равнобедренный"
        if type == 10:
            return "Равнобедренный"
        return "Разносторонний"
    
    # возвращает периметр треугольника
    def perimetr (self):
        return self.a + self.b + self.c
    
    # возвращает площадь треугольника по трем сторонам - по формуле Герона
    def area (self):
        p = self.perimetr()/2 # <- полупериметр
        area = (p * (p - self.a) * (p-self.b) * (p - self.c)) ** 0.5
        return area
        


# ------------------ БЛОК ЗАПУСКА ---------------------

t1 = Triangle (5)
t2 = Triangle (5, 10)
t3 = Triangle (2, 3, 4)
t4 = Triangle (3, 4, 5)
t5 = Triangle (8, 6)

for t in [t1, t2, t3, t4, t5]:
    print (f"{t.get_sides ()}, {t.get_type ()}, периметр: {t.perimetr()}, площадь: {round (t.area (), 2)}")

# попытка создания треугольника с заведомо не правильными параметрами
t6 = Triangle (25, 10, 14)
t7 = Triangle (25, -14, 14)