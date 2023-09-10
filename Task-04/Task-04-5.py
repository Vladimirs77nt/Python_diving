# Задание №5

# Функция принимает на вход три списка одинаковой длины:
#   имена str, 
#   ставка int, 
#   премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения. 
# ✔ Сумма рассчитывается как ставка умноженная на процент премии. 

def function_1 (name_, stavka_, prem_):
    dict_worker = {}
    for index, name in enumerate(name_):
        dict_worker[name] = (stavka_[index] * float(prem_[index][0:-1]) / 100)
    return dict_worker

def function_2 (name_, stavka_, prem_):
    return {name_[i]: (stavka_[i] * float(prem_[i][0:-1]) / 100) for i in range (len(name_))}


name = ["Иван", "Василий", "Дмитрий"]
stavka = [20000, 30000, 25000]
prem = ["10.25%", "8.0%", "15%"]

print (function_1(name, stavka, prem))
print (function_2(name, stavka, prem))