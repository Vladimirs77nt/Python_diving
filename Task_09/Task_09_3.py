# Задание №3

# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат,
# который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

import json
import os
from typing import Callable


def decor (func: Callable):
    def wrapper (*args, **kwargs):
        file_name = func.__name__ + ".json"
        with open (file_name, "r", encoding="utf-8") as file:
            try:
                data = json.load (file)
            except json.JSONDecodeError:
                data = {}
        result = str (func (*args, **kwargs))
        data [result] = list (args + tuple(kwargs.items()))
        with open (file_name, "w", encoding="utf-8") as file:
            json.dump (data, file, indent=4, ensure_ascii=False )
        return result
    return wrapper

@decor
def factorial (x):
    f = 1
    for i in range (2, x+1):
        f *= i
    return f


# ----------------------------- 

print (factorial (5))
print (factorial (10))
print (factorial (15))
print (factorial (x=5))
print (factorial (15))
print (factorial (15))
print (factorial (15))
print (factorial (x = 10))
print (factorial (x = 0))