# Задание №8

# Нарисовать в консоли ёлку спросив у пользователя количество рядов.

# Пример результата:
# Сколько рядов у ёлки? 5
#       *
#      ***
#     *****
#    *******
#   *********

row  = int (input("Сколько рядов у ёлки? "))

for i in range(row):
    line = ""
    for j in range(row*2-1):
        if j<(row-i-1) or j>(row+i-1):
            line += " "
        else:
            line += "*"
    print (line)