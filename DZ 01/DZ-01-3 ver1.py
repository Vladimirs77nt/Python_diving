# Домашнее задание №3

# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
#     from random import randint
#     num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

hidden_number = randint(0, 1001)
count = 0
number_attempts = 10

print()
print ("Загадано число от 0 до 1000 - попробуйте отгадать его меньше чем за 10 попыток")
print()

while True:
    count += 1
    print ("Попытка №", count)
    num  = int (input("Введите число от 0 до 1000: "))
    if num <0 or num>1000:
        print ("Введено неверное число!")
    elif num == hidden_number:
        print(">>> Ты угадал число! за", count, "попыток")
        print()
        break
    elif num>hidden_number:
        print("Меньше!")
    elif num<hidden_number:
        print("Больше!")
    if count == number_attempts:
        print()
        print("Ты проиграл! Попытки исчерпаны...")
        print("... а число было загадано =", hidden_number)
        break
    print()