# Задание №4

# ✔ Функция получает на вход список чисел. 
# ✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок. 
# ✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии.

import random

def sort_buble (list_num):
    len_list = len(list_num)
    for i in range(0, len_list-1):
        for j in range (i+1, len_list):
            if list_num[i] > list_num[j]:
                list_num[i], list_num[j] = list_num[j], list_num[i]

num = [random.randint(0, 20) for _ in range (10)]
print (num)
sort_buble(num)
print (num)