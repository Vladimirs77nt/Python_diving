# Домашнее задание №2

# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу и на себя».
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

while True:
    composite = False
    num  = int (input("Введите число от 0 до 100.000: "))
    if num <0 or num>100000:
        print ("Введено неверное число!")
    for i in range (2, int(num/2)):
        if num%i == 0:
            print("Число составное")
            composite = True
            break
    if not composite:
        print("Число простое")