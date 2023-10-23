# Задание №3

# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

# ВЕРСИЯ 2


class FactorialGen:

    def __init__(self, start, stop=None, step=1):
        if step is None:
            start, step = 1, start
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start
    
    def _factorial (self, num):
        if num == 0:
            return 1
        result = 1
        for i in range (self.start, num+1, self.step):
            result *= i
        return result
    
    def __iter__ (self):
        return self
    
    def __next__ (self):
        if self.current > self.stop:
            raise StopIteration
        result = self._factorial(self.current)
        self.current += self.step
        return result


fact = FactorialGen(2, 20, 2)
for i in fact:
    print (i)