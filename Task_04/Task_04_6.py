# Задание №6

# ✔ Функция получает на вход список чисел и два индекса. 
# ✔ Вернуть сумму чисел между между переданными индексами. 
# ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

import random

def function_1 (list_num, index_1, index_2):
    index_1, index_2 = sorted([index_1, index_2])
    if index_1 < 0:
        index_1 = 0
    if  index_2 > len(list_num)-1:
        index_2 = len(list_num)-1
    summ = 0
    for i in range (index_1, index_2+1):
        summ += list_num [i]
    return summ

def function_2 (list_num, index_1, index_2):
    index_1, index_2 = sorted([index_1, index_2])
    return sum(list_num[index_1:index_2])

num = [random.randint(0, 20) for _ in range (10)]
print (num)
print (function_1(num, -10, 50))
print (function_2(num, -10, 100))