# Задание 1

# Напишите функцию для транспонирования матрицы

# функция печати матрицы
def matrix_print (matrix):
    for row in matrix:
        print (' '.join(map(str,row)))

# функция транспонирования матрицы
def matrix_transposition (matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# задаем исходную матрицу 
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]

print ()
print (" -- исходная матрица ---")
matrix_print (matrix)
print ()

matrix = matrix_transposition(matrix)
print (" -- транспонированная матрица ---")
matrix_print (matrix)
print ()