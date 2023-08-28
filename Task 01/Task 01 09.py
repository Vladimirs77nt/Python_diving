# Задание №9

# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

print("{:^60s}".format("ТАБЛИЦА УМНОЖЕНИЯ"))

for j in range (2, 11):
    for i in range (2, 6):
        print("{:>2d} X {:^2d} = {:^2d}   ".format(i, j, i*j), end = "")
    print()

print ()

for j in range (2, 11):
    for i in range (6, 10):
        print("{:>2d} X {:^2d} = {:^2d}   ".format(i, j, i*j), end = "")
    print()

print ()