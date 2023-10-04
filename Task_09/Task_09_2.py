# Задание №2

# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

from random import randint
from typing import Callable

def decorator (game: Callable):
    def wrapper (*args, **kwargs):
        max, count, *_ = args
        if not (0 < max < 101):
            max = randint (1, 100)
            print (f"Верхний предел загадываемого числа изменен на {max}")
        else: print ("+")
        if not (0 < count < 11):
            count = randint (1, 10)
            print (f"Количество попыток на отгадывание изменено на {count}")
        else: print ("+")
        return game (max, count)
    
    return wrapper

@decorator
def ugadai_chislo (max, count):
    min = 0
    hidden_number = randint (min, max)
    count_max = count
    print()
    print (f"Загадано число от {min} до {max} - попробуйте отгадать его меньше чем за {count} попыток")
    print()
    while True:
        num  = int (input(f"Введите число от {min} до {max}: "))
        if num <min or num>max:
            print ("Введено неверное число!")
        elif num == hidden_number:
            print(f">>> Ты угадал число! за {count_max - count + 1} попыток")
            print()
            return True
        elif num>hidden_number:
            print("Меньше!")
        elif num<hidden_number:
            print("Больше!")
        count -= 1
        if count <= 0:
            print()
            print("Ты проиграл! Попытки исчерпаны...")
            print("... а число было загадано =", hidden_number)
            return False
        print(f" ..осталось {count} попыток...")
        print()


# ----- БЛОК ЗАПУСКА ---------------------

print ( ugadai_chislo (1000, 1000))