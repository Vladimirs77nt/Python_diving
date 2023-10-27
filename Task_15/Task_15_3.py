# Задание №3

# Доработаем задачу 2.

#     Сохраняйте в лог файл раздельно:
#     ○ уровень логирования,
#     ○ дату события,
#     ○ имя функции (не декоратора),
#     ○ аргументы вызова,
#     ○ результат.

import logging
from time import asctime
from typing import Callable
from functools import wraps

def decor (func: Callable):
    logger = logging.getLogger(__name__)
    logging.basicConfig (filename="Task_15/my_log_3.log", filemode="w", encoding="utf-8",
                         level=logging.INFO, style="{")
    @wraps(func)
    def wrapper (*args, **kwargs):
        result = str (func (*args, **kwargs))
        logger.info(f"{asctime} - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s result: {result}, *args: {args}, *kwargs: {kwargs}")
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