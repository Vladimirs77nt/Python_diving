# Задание №1

# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# Например - отлавливаем ошибку деления на ноль.

import logging

logger = logging.getLogger(__name__)
format = "{asctime:<20} - {levelname:<10} - {msg}"

logging.basicConfig (filename="Task_15/my_log_1.log", filemode="w", encoding="utf-8", level=logging.ERROR,
                     style="{", format=format)
def func(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        logger.error(msg=e)

func (100, 0)
