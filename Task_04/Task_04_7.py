# Задание №7

# ✔ Функция получает на вход словарь с названием компании в качестве ключа 
# и списком с доходами и расходами (3-10 чисел) в качестве значения. 
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании 
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

def profitable_status_1 (data: dict) -> bool:
    for name, profit in data.items():
        if sum(profit)<0:
            return False
    return True

def profitable_status_2 (data: dict) -> bool:
    for i in data:
        data[i] = sum(data[i])
    return all(map(lambda x: x>0, data.values()))

data = {"Abibas": [1000, 2000, 3000, -3500, 1500],
        "Hike": [5000, 1000, -300, -500, -1000],
        "Rybek": [300, 200, 300, -500, -1000],
        }

print (profitable_status_1 (data))
print (profitable_status_2 (data))