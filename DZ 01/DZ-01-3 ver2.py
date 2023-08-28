# Домашнее задание №3 - вторая версия

# Пользователь загадывает число от 0 до 1000. Компьютер пытается его угадать за 10 попыток.

count = 0
number_attempts = 10

print()
hidden_number  = int (input("Загадайте число от 0 до 1000: "))
print()

low_number = 0
hight_number = 1000

while True:
    count += 1
    print ("Попытка №", count)
    guessed_number = int((hight_number + low_number)/2)
    print ("Число =", guessed_number)

    if guessed_number == hidden_number:
        print(">>> КОМПЬЮТЕР угадал число! за", count, "попыток")
        print()
        break
    elif guessed_number>hidden_number:
        print("Меньше!")
        hight_number = guessed_number
    elif guessed_number<hidden_number:
        print("Больше!")
        low_number = guessed_number
    if count == number_attempts:
        print()
        print("Компьютер проиграл! Попытки исчерпаны...")
        print("... а число было загадано =", hidden_number)
        break
    print()