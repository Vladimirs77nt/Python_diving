# Задание №4

# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции

import json
import os
from typing import Callable

def decor_area (area=0):
    area = abs (area)

    def decor (func: Callable):

        def wrapper (x):
            full_result = ""
            for i in range (x-area, x+area+1): # верхний предел факторила
                if i < 1:
                    continue
                result = func (i)
                line = ""
                for j in range (1, i):
                    line += str(j) + " х "
                line += str (i) + " = " + str (result)
                full_result += line + "\n"
            return full_result
        return wrapper
    return decor

@decor_area(5)
def factorial (x):
    f = 1
    for i in range (2, x+1):
        f *= i
    return f

# ----- БЛОК ЗАПУСКА ---------------------

a = factorial (10)
print (a)