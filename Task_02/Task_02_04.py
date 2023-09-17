# Задание №4

# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру. 
# Диаметр не превышает 1000 у.е. Точность вычислений должна составлять не менее 42 знаков после запятой.

import math
import decimal

diameter = int(input("Введите диаметр (до 1000): "))

decimal.setcontext = 6
area = decimal.Decimal(math.pi * ((diameter/2) ** 2))
lenght = decimal.Decimal(math.pi * diameter)

print ("площадь:",area)
print ("длина окружности:",lenght)