# Задание №1

# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
# пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.

def input_number ():
    while True:
        num = input ("Введите число: ")
        try:
            num = float (num)
            return int(num) if int(num) == num else num
        except Exception as e:
            print ("Вы ввели не число! повторите!")
    

print (input_number ())