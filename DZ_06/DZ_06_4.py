# Задача 4

# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

from modules.chess import queens_list_random_8          # функция генерирует 8 пар ферзей, которые не бьют друг друга
from modules.chess import check_placement_queens_list   # функция определяет 8 пар ферзей - ферзи не бьют друг друга?
from modules.chess import print_сhess_table             # функция печатает шахматную доску по списку ферзей с координатами

# модуль modules.chess:
# print_сhess_table(list_pairs): - функция печати шахматной доски 8х8 -> на входе список ферзей с координатами
# queens_list_random (): - функция формирования списка со случайной (рандомной) расстановкой 8 ферзей -> на ВЫХОДЕ список ферзей с координатами
# queens_list_random_8 (): - функция формирования списка c гарантированной расстановкой из 8 ферзей -> на ВЫХОДЕ список ферзей с координатами
# check_placement_queens_list (list_pairs): - функция определяет не бьют ли 8 ферзей из списка друг друга? -> True или False
# _place_battle (_chess_board, x, y): - защищенная функция определения всех клеток, которые будут находится под ударом ферзя
# _placement_chess_table_list (list_pairs): - формирование доски 8х8 -> на входе список ферзей с координатами

print ("-----------------------------------\n")
print (" --- ГЕНЕРИРУЕМ 4 списка ферзей со случайной, но с ГАРАНТИРОВАННОЙ расстановкой !!! ---\n")
count = 4
for i in range(count):
    print (f" гарантированный список №{i+1}:\n")
    list_queens = queens_list_random_8()
    print_сhess_table(list_queens)
    print(f"\nПроверка расстановки: {check_placement_queens_list(list_queens)}")
    print ("\n-----------------------------------\n")