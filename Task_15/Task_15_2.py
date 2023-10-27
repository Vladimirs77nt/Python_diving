# Задание №2

# На семинаре #9 про декораторы был создан логирующий декоратор.
# Он сохранял аргументы функции и результат её работы в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging.

    # Семинар 9 - Задание №3

    # Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат,
    # который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
    # Каждый ключевой параметр сохраните как отдельный ключ json словаря.
    # Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
    # Имя файла должно совпадать с именем декорируемой функции.

import logging
import os
from typing import Callable


def decor (func: Callable):
    my_format = '{msg}'
    logger = logging.getLogger(__name__)
    logging.basicConfig (filename="Task_15/my_log_2.log", filemode="w", encoding="utf-8",
                         level=logging.INFO, style="{", format=my_format)
    def wrapper (*args, **kwargs):
        result = str (func (*args, **kwargs))
        logger.info(f"result: {result}, *args: {args}, *kwargs: {kwargs}")
        return result
    return wrapper

@decor
def factorial (x):
    f = 1
    for i in range (2, x+1):
        f *= i
    return f

# ----- БЛОК ЗАПУСКА ---------------------

print (factorial (5))
print (factorial (10))
print (factorial (15))
print (factorial (x=5))
print (factorial (15))
print (factorial (15))
print (factorial (15))
print (factorial (x = 10))
print (factorial (x = 0))