# ТЕСТ 4.

# Задача о матричных операциях

# Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые операции с матрицами.

# Атрибуты класса:
#   * rows (int): Количество строк в матрице.
#   * cols (int): Количество столбцов в матрице.
#   * data (list): Двумерный список, содержащий элементы матрицы.

# Методы класса:
#   * __init__(self, rows, cols): Конструктор класса, который инициализирует атрибуты rows и cols, а также создает двумерный список data размером rows x cols и заполняет его нулями.
#   * __str__(self): Метод, возвращающий строковое представление матрицы. Возвращаемая строка представляет матрицу, где элементы разделены пробелами, а строки разделены символами новой строки. Например:
# 1 2 3
# 4 5 6
#   * __repr__(self): Метод, возвращающий строковое представление объекта, которое может быть использовано для создания нового объекта того же класса с такими же размерами и данными.
#   * __eq__(self, other): Метод, определяющий операцию "равно" для двух матриц. Сравнивает две матрицы и возвращает True, если они имеют одинаковое количество строк и столбцов, а также все элементы равны. Иначе возвращает False.
#   * __add__(self, other): Метод, определяющий операцию сложения двух матриц. Проверяет, что обе матрицы имеют одинаковые размеры (количество строк и столбцов). Если размеры совпадают, создает новую матрицу, где каждый элемент равен сумме соответствующих элементов входных матриц.
#   * __mul__(self, other): Метод, определяющий операцию умножения двух матриц. Проверяет, что количество столбцов в первой матрице равно количеству строк во второй матрице. Если условие выполняется, создает новую матрицу, где элемент на позиции [i][j] равен сумме произведений элементов соответствующей строки из первой матрицы и столбца из второй матрицы.


from random import randint as rnd

# класс Матрица
class Matrix:

    # метод инициализации матрицы
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        if not data:  # <- создаем пустую матрицу, если в параметрах не передана
            self.data = []
            # заполняем матрицу нулями
            for row in range(self.rows):
                self.data.append([])
                for _ in range(self.cols):
                    self.data[row].append(0)
        else:
            self.data = data

    # метод заполнения матрицы случайными числами от (min) до (max)
    def randint_matrix (self, min, max=None):

        if not max: # <- если передан один аргумент - значит это max, а min = 0
            max = min
            min = 0

        for row in range(self.rows):
            self.data.append([])
            for col in range(self.cols):
                self.data[row][col] = rnd(min, max)

    # метод сложения матриц
    def __add__ (self, other):
        matrix_new = []
        for row in range (self.rows):
            matrix_new.append([])
            for col in range (self.cols):
                matrix_new[row].append(self.data[row][col] + other.data[row][col])
        return Matrix(self.rows, self.cols, matrix_new)
    
    # метод УМНОЖЕНИЯ матриц
    def __mul__ (self, other):
        len = self.rows
        matrix_new = []
        for i in range (self.rows):
            matrix_new.append([])
            for _ in range(other.cols):
                matrix_new[i].append(0)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    # resulted matrix
                    matrix_new[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(self.rows, other.cols, matrix_new)

    def __str__ (self):
        line_rows = None
        for i in range(self.rows):
            if line_rows:
                line_rows += "\n"
            else:
                line_rows = ""
            line = ""
            for j in range(self.cols-1):
                line = line + str(self.data[i][j]) + " "
            line = line + str(self.data[i][self.cols-1])
            line_rows += line
        return line_rows
    
    def __repr__ (self):
        line_rows = None
        for i in range(self.rows):
            if line_rows:
                line_rows += "], "
            else:
                line_rows = "["
            line = "["
            for j in range(self.cols-1):
                line = line + str(self.data[i][j]) + ", "
            line = line + str(self.data[i][j+1])
            line_rows += line
        line_rows += "]]"
        return f"Matrix({self.rows}, {self.cols}, {line_rows})"
    
    def __eq__ (self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

# ------------------ БЛОК ЗАПУСКА ---------------------

# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)
print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)