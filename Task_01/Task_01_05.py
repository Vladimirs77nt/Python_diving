# Задание №5

# 📌 Работа в консоли в режиме интерпретатора Python.
# 📌 Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# 📌 Используйте while и if.
# 📌 Попробуйте разные значения e и n. 

n = 13
e = 3
count = 0
summ = 0
while count < n:
    count += 1
    if count%2 != 0 or count%e == 0:
        continue
    print (count)
    summ += count
print("Сумма =", summ)