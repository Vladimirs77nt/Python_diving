# Задача 3

# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random

# функция печати шахматной доски
def print_сhess_table(list_pairs):
    
    # формируем шахматную доску по списку фрезей с координатами
    _chess_board = _placement_chess_table_list (list_pairs)

    # тип клетки - белая или черная
    square_type = 1 

    print("   A B C D E F G H")
    for y in range (8):
        str_line = (f"{8-y}  ")
        square_type = -square_type
        for x in range (8):
            if _chess_board[y][x] != 1:
                if square_type == -1:
                    str_line = str_line + chr (9632) + " "
                else:
                    str_line = str_line + chr (9633) + " "
            elif _chess_board[y][x] == 1:
                str_line = str_line + (f"\033[31m{chr (9819)}\033[0m") + " "
            square_type = -square_type # меняем тип клетки
        print(str_line)

# формирование доски по переданному списку ферзей
def _placement_chess_table_list (list_pairs):
    # заполнение доски 8х8 нулями - пустые поля
    _chess_board = [[0 for _ in range (8)] for _ in range (8)]
    for queen in list_pairs:
            _chess_board [queen[0]][queen[1]] = 1      # ставим ферзя - цифра 1 в клетке
    return _chess_board

# функция формирования списка со случайной (рандомной) расстановкой 8 ферзей
def queens_list_random ():
    queens_list = []
    # row - ряды, перебираем от 0 до 7
    for row in range (7):
        # col - столбцы, выбираем случайно от 0 до 7
        col = random.randint (0,7)
        queens_list.append([row, col])
    return queens_list
    # возвращает сформированную доску, если найдена комбинация из 8 ферзей

# функция формирования списка c гарантированной расстановкой из 8 ферзей
def queens_list_random_8 ():
    while True:
        queens_list = []
        queen = 0
        # заполнение доски 8х8 нулями - пустые поля
        _chess_board = [[0 for _ in range (8)] for _ in range (8)]
        # row - ряды, перебираем от 0 до 7
        for row in range (8):
            # col - столбцы, перебираем перемешанный список из 8 цифр
            list_random = list(i for i in range (8))
            random.shuffle (list_random)
            for col in list_random:
                if _chess_board [row][col] == 0:
                    _chess_board [row][col] = 1      # ставим ферзя - цифра 1 в клетке
                    queens_list.append([row, col])
                    _chess_board = _place_battle (_chess_board, row, col)
                    queen += 1
                    break
        if queen == 8:
            return queens_list
            # возвращает сформированную доску, если найдена комбинация из 8 ферзей

# функция определяет не бьют ли 8 ферзей из списка друг друга?
def check_placement_queens_list (list_pairs):
    if len (list_pairs) != 8:
        return False
    queen = 0 # кол-во проверенных ферзей
    # заполнение доски 8х8 нулями - пустые поля
    _chess_board = [[0 for _ in range (8)] for _ in range (8)]
    for i in list_pairs:
        if _chess_board [i[0]][i[1]] == 0:
            _chess_board [i[0]][i[1]] = 1      # ставим ферзя - цифра 1 в клетке
            _chess_board = _place_battle (_chess_board, i[0], i[1])
            queen += 1
    return queen == 8

# защищенная функция определения всех клеток, которые будут находится под ударом ферзя
def _place_battle (_chess_board, x, y):

    x1 = x          # двигаемся направо
    y2 = y          # двигаемся направо
    x3, y3 = x, y   # двигаемся направо вверх
    x4, y4 = x, y   # двигаемся направо вниз
    x5 = x          # двигаемся налево
    y6 = y          # двигаемя ввверх
    x7, y7 = x, y   # двигаемся налево вверх
    x8, y8 = x, y   # двигаемся налево вниз

    # если клетка под ударом - ставим цифру -1
    for i in range (1,8):
        
        # двигаемся направо
        if x1<7:
            x1 += 1
            _chess_board [x1][y] = -1

        # двигаемся направо
        if y2<7:
            y2 += 1
            _chess_board [x][y2] = -1

         # двигаемся направо вверх
        if x3<7 and y3>0:
            x3 += 1
            y3 -= 1
            _chess_board [x3][y3] = -1

        # двигаемся направо вниз
        if x4<7 and y4<7:
            x4 += 1
            y4 += 1
            _chess_board [x4][y4] = -1

        # двигаемся налево
        if x5>0:
            x5 -= 1
            _chess_board [x5][y] = -1

        # двигаемя ввверх
        if y6>0:
            y6 -= 1
            _chess_board [x][y6] = -1

        # двигаемся налево вверх
        if x7>0 and y7>0:
            x7 -= 1
            y7 -= 1
            _chess_board [x7][y7] = -1

        # двигаемся налево вниз
        if x8>0 and y8<7:
            x8 -= 1
            y8 += 1
            _chess_board [x8][y8] = -1
        
    return _chess_board