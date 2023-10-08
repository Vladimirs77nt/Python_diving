# Задание

# 1. Решить задания, которые не успели решить на семинаре.
# 2. Доработаем задания 5-6. Создайте класс-фабрику:
#     Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
#     Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# 3. Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
#     Превратите функции в методы класса, а параметры в свойства.
#     Задания должны решаться через вызов методов экземпляра.

# КЛАСС МАТРИЦА


from random import randint as rnd


# класс Матрциа
class Matrix:

    # метод инициализации матрицы
    def __init__(self, rows, columns, matrix=None):
        self.rows = rows
        self.columns = columns
        if not matrix:  # <- создаем пустую матрицу, если в параметрах не передана
            self.matrix = []
            # заполняем матрицу нулями
            for row in range(self.rows):
                self.matrix.append([])
                for _ in range(self.columns):
                    self.matrix[row].append(None)
        else:
            self.matrix = matrix

    # метод печати матрицы
    def print_matrix (self):
        line = " "*6
        for col in range(self.columns):
            line += f"\033[31m{str(col):^6}\033[0m"
        print (line)
        for row in range(self.rows):
            line = f"\033[31m{str(row):^5}\033[0m"
            for col in range(self.columns):
                item = self.matrix[row][col]
                line += f"{str(item):^6}"
            print (line)

    # метод заполнения матрицы случайными числами от (min) до (max)
    def randint_matrix (self, min, max=None):

        if not max: # <- если передан один аргумент - значит это max, а min = 0
            max = min
            min = 0

        for row in range(self.rows):
            self.matrix.append([])
            for col in range(self.columns):
                self.matrix[row][col] = rnd(min, max)

    # метод транспонирования матрицы "in place"
    def transposition_matrix (self):
        matrix_new = []
        for col in range (self.columns):
            matrix_new.append([])
            for row in range (self.rows):
                matrix_new[col].append(self.matrix[row][col])
        self.columns, self.rows = self.rows, self.columns
        self.matrix = matrix_new
    

# ------------------ БЛОК ЗАПУСКА ---------------------

matrix_1 = Matrix(3,6)            # <- создаем пустую матрицу 3х6
print ()

matrix_1.randint_matrix (10, 99)  # <- заполняем случайными числами от 10 до 99
matrix_1.print_matrix()
print ()

matrix_1.transposition_matrix ()  # <- транспонируем матрицу
matrix_1.print_matrix()
print ()