# Домашнее задание №2 (семинар 2)

# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions

# функция возврата НАИБОЛЬШЕГО ОБЩЕГО ДЕЛИТЕЛЯ (НОД)
def nod_f (a, b):
    if a % b == 0:
        return b
    if b % a == 0:
        return a
    if a > b:
        return(nod_f((a % b), b))
    else:
        return(nod_f(a, (b % a)))

# функция возврата НАИМЕНЬШЕГО ОБЩЕГО КРАТНОГО (НОК)
def nok_f (a, b):
    return int(a*b/nod_f(a, b))

# функция сокращения дроби
def reduction (f):
    while nod_f(f[0], f[1])>1:
        nod = nod_f(f[0],f[1])
        f = [int(f[0]/nod), int(f[1]/nod)]
    return f

# ====================================================

print ()
fraction1 = input("Введите 1-ую дробь вида a/b: ")
fraction2 = input("Введите 2-ую дробь вида a/b: ")

# Cплитуем введенные строки, переводим строковые значения в числа (int)
fraction1 = fraction1.split("/")
fraction1[0] = int(fraction1[0])
fraction1[1] = int(fraction1[1])

fraction2 = fraction2.split("/")
fraction2[0] = int(fraction2[0])
fraction2[1] = int(fraction2[1])

# Найдем наименьшее общее кратное знаменателей (далее — НОК) для определения единого делителя. 
nok = nok_f(fraction1[1], fraction2[1])

# Найдем дополнительные множители для каждой дроби. Для этого НОК делим на каждый знаменатель: 
k1 = int(nok/fraction1[1])
k2 = int(nok/fraction2[1])

# Воспользуемся одним из основных свойств дробей: перемножим делимое и делитель на дополнительный множитель.
# После умножения делитель должен быть равен наименьшему общему кратному (нок), которое мы ранее высчитывали.
# Затем можно перейти к сложению. 
f_summ = [fraction1[0]*k1 + fraction2[0]*k2, nok]                             # СУММА ДРОБЕЙ (не сокращенная)

# Если есть что сократить - выполняем сокращение.
f_summ = reduction (f_summ)

# перемножение дробей
f_composition = (fraction1[0] * fraction2[0], fraction1[1] * fraction2[1])    # ПРОИЗВЕДЕНИЕ ДРОБЕЙ (не сокращенная)

# Если есть что сократить - выполняем сокращение.
f_composition = reduction (f_composition)

# ВЫВОДИМ РЕЗУЛЬТАТ
print ()
print (" > Сумма дробей:", f_summ[0], "/", f_summ[1])
print (" > Произведение дробей:", f_composition[0], "/", f_composition[1])
print ()

# ПРОВЕРКА
print (" --- ПРОВЕРКА - модуль fractions ---")

f1 = fractions.Fraction(fraction1[0], fraction1[1])
f2 = fractions.Fraction(fraction2[0], fraction2[1])
f_summ = f1 + f2
f_composition = f1 * f2
print ()
print (" > Сумма дробей:", f_summ)
print (" > Произведение дробей:", f_composition)
print ()