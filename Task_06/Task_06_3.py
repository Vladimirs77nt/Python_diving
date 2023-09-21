# Задание 3
# Улучшаем задачу 2.

# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

from modules.guess import func_ugadai as guess_game
import sys

args = list (map (int, sys.argv[1:]))

if len(args) == 3:
    min = args[0]
    max = args[1]
    count = args[2]
elif len(args) == 2:
    min = args[0]
    max = args[1]
    count = 6
elif len(args) == 1:
    min = 0
    max = args[0]
    count = 6
else:
    min = 0
    max = 100
    count = 6

guess_game (min, max, count)