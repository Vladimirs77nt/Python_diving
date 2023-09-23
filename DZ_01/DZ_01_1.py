# Домашнее задание №1

# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c — стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с
# суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника 
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, 
# равнобедренным или равносторонним. 

a = 3
b = 6
c = 5

if (a + b > c) & (a + c > b) & (b + c > a):
    if a == b == c:
        print("Треугольник равносторонний")
    if ((a ** 2 + b ** 2) == c ** 2) or ((c ** 2 + b ** 2) == a ** 2) or ((a ** 2 + c ** 2) == b ** 2):
        print("Треугольник прямоугольный")
    if (a == b) or (b == c) or (a == c):
        print("Треугольник равнобедренный")
    else:
        print("Разносторонний треугольник")
else:
    print("Треугольника с заданными сторонами не существует")