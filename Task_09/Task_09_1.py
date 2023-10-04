# Задание №1

# Создайте функцию-замыкание, которая запрашивает два целых числа:
#  - от 1 до 100 для загадывания,
#  - от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток. 

from random import randint

def igra ():

    min = 0
    # max = 100
    max = int (input ("Введите число до скольки можно загадать? = "))
    # count = 7
    count = int (input ("Сколь попыток разрешается? = "))
    
    hidden_number = -1
    if hidden_number < 0:
            hidden_number = randint (min, max)

    def func_ugadai ():
        nonlocal min, max, hidden_number, count
        print()
        print (f"Загадано число от {min} до {max} - попробуйте отгадать его меньше чем за {count} попыток")
        print()
        while True:
            num  = int (input(f"Введите число от {min} до {max}: "))
            if num <min or num>max:
                print ("Введено неверное число!")
            elif num == hidden_number:
                print(">>> Ты угадал число! за", count, "попыток")
                print()
                break
            elif num>hidden_number:
                print("Меньше!")
            elif num<hidden_number:
                print("Больше!")
            count -= 1
            if count <= 0:
                print()
                print("Ты проиграл! Попытки исчерпаны...")
                print("... а число было загадано =", hidden_number)
                break
            print(f" ..осталось {count} попыток...")
            print()

    return func_ugadai


# ----- БЛОК ЗАПУСКА ---------------------

primer = igra ()

primer ()
primer ()