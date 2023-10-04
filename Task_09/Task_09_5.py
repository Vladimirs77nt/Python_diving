# Задание №5

# Объедините функции из прошлых задач. Функцию угадайку задекорируйте:
#   ○ декораторами для сохранения параметров,
#   ○ декоратором контроля значений и
#   ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.

from random import randint
from typing import Callable
import json
import os

# ----- ДЕКОРАТОР МНОГОКРАТНОГО ВЫЗОВА ------

def decor_couter (count: int):
    def decor_couter_inner (func: Callable):
        def wrapper (*args, **kwargs):
            res = []
            for i_count in range (count):
                print (f"{i_count=}, {func}")
                res.append (func (*args, **kwargs))
            return res
        return wrapper
    return decor_couter_inner


# ----- ДЕКОРАТОР ЗАПИСИ ПАРАМЕТРОВ ------
def decor_param (func: Callable):
    def wrapper (*args, **kwargs):
        file_name = func.__name__ + ".json"
        try:
            with open (file_name, "r", encoding="utf-8") as file:
                data = json.load (file)
        except FileNotFoundError:
            data = {}
        result = str (func (*args, **kwargs))
        data [result] = list (args + tuple(kwargs.items()))
        with open (file_name, "w", encoding="utf-8") as file:
            json.dump (data, file, indent=4, ensure_ascii=False )
        return result
    return wrapper

# ----- ДЕКОРАТОР КОНТРОЛЯ ВВЕДЕННЫХ ДАННЫХ ------
def decor_limits (func: Callable):
    def wrapper (*args, **kwargs):
        min, max, count, *_ = args
        if not (0 < max < 101):
            max = randint (1, 100)
            print (f"Верхний предел загадываемого числа изменен на {max}")
        if not (0 < count < 11):
            count = randint (1, 10)
            print (f"Количество попыток на отгадывание изменено на {count}")
        return func (min, max, count)
    return wrapper

# ----- ИГРА ------
@decor_couter(3)
@decor_param
@decor_limits
def ugadai_chislo (min, max, count):
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
            result = f"😀 Ты угадал число ({hidden_number})! за {count_max - count + 1} попыток"
            print (result)
            print()
            return result # <--------------- ВЫХОД если угадал
        elif num>hidden_number:
            print("Меньше!")
        elif num<hidden_number:
            print("Больше!")
        count -= 1
        if count <= 0:
            print()
            result = f"😏 Ты проиграл... Попытки исчерпаны, а число было загадано: {hidden_number}"
            print (result)
            print()
            return result # <---------------- ВЫХОД  если проиграл
        print(f" ..осталось {count} попыток...")
        print()


# ----- БЛОК ЗАПУСКА ---------------------

dir_path = os.getcwd() + "/Task_09"    # <-- рабочая папка для работы
os.chdir(dir_path)

ugadai_chislo (0, 10, 3)