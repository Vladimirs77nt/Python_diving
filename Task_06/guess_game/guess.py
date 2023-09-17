# модуль программы угадай число с тремя входными параметрами

from random import randint

def func_ugadai (min=0, max=100, count_max=6, *_):
    hidden_number = randint(min, max)
    count = 0
    
    print()
    print (f"Загадано число от {min} до {max} - попробуйте отгадать его меньше чем за {count_max} попыток")
    print()

    while True:
        count += 1
        print ("Попытка №", count)
        num  = int (input(f"Введите число от {min} до {max}: "))
        if num <min or num>max:
            print ("Введено неверное число!")
        elif num == hidden_number:
            print(">>> Ты угадал число! за", count, "попыток")
            print()
            return True
        elif num>hidden_number:
            print("Меньше!")
        elif num<hidden_number:
            print("Больше!")
        if count == count_max:
            print()
            print("Ты проиграл! Попытки исчерпаны...")
            print("... а число было загадано =", hidden_number)
            return False
        print()