# Задача №3

# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Напишите программу банкомат. 
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой 
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

def print_menu ():
    print (" --- МЕНЮ БАНКОМАТА ---")
    print (" > выберите:")
    print ("1. Пополнить счет")
    print ("2. Снять")
    print ("3. Выйти")
    