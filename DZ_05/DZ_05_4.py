# Задача 4

# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

# функция-генератор = возвращает следующее число Фибоначчи (стартует от 0)
def func ():
    previous = 0
    current = 0
    while True:
        previous = current
        current = summ
        if current == 0:
            yield 0
            yield 1
            current = 1
        summ = previous + current
        yield summ
        
# запуск
fibo_number = func()
for i in range (20):
    print (f"{i+1:>5}:  {next(fibo_number)}")