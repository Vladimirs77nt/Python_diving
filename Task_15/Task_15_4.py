# Задание №4

# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

import logging
import datetime
from time import asctime


dict_weekday = {"понедельник": 1,
                "вторник": 2,
                "среда": 3,
                "четверг": 4,
                "пятница": 5,
                "суббота": 6, 
                "воскресенье": 7}

dict_month = {"января": 1,
              "февраяля": 2,
              "марта": 3,
              "апреля": 4,
              "мая": 5,
              "июня": 6, 
              "июля": 7,
              "августа": 8,
              "сентября": 9,
              "октября": 10,
              "ноября": 11, 
              "декабря": 12}

def func (data_str):
    data_str = data_str.split()
    now_year = datetime.datetime.now().year     # текущий год
    num_weekday = int(data_str[0][0])           # номер недели
    num_day = dict_weekday [data_str[1]]        # день недели
    num_month = dict_month [data_str[2]]        # месяц

    day_one_month = datetime.datetime.strptime(f'{now_year}-{num_month}-01', '%Y-%m-%d').weekday()
    # номер дня недели 1-го числа в месяце (0-понедельник, 6-воскресенье)

    day_relative = (num_weekday-(1 if day_one_month<num_day else 0))*7 + num_day
    # относительный день в месяце (если считать 1 день любого месяца - понедельником)

    day = day_relative - day_one_month
    # фактический день в месяце = относительный день минус номер дня недели 1-го числа в месяце

    result_date = datetime.datetime.strptime(f'{now_year}-{num_month}-{day}', '%Y-%m-%d').strftime("%Y-%m-%d")
    return result_date


# ----------------------------------------------------------------------
my_format = "{asctime:<15} - {levelname:<10} - {msg}"
logging.basicConfig(filename='Task_15/my_log_4.log', filemode='w', encoding='utf-8',
                    level=logging.INFO, style='{', format=my_format)
logger = logging.getLogger(__name__)

date_list = ["4-ый четверг октября",
             "1-ый понедельник ноября",
             "5-ая суббота сентября",
             "1-ый вторник мая",
             "5-ая суббота марта",
             "5-ый четверг июня"]
for i_date in date_list:
    try:
        data_res = func(i_date)
        print (f"{i_date}\t{data_res}")
        logger.info (msg=f"{i_date:.<30}{data_res}")
    except ValueError as e:
        print (f"{i_date}\t<- ошибка даты!")
        logger.error (msg=f"{i_date:.<30}!ошибка даты!")