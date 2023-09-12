# Задание №2

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

import re
from ast import literal_eval
from re import sub as re_sub

def func_dict_hash (data):
    string = str(globals())
    index_start = re.search(r'\b(dict_key)\b', string).end()+3
    item_str = string[index_start:-1]
    print ((item_str), type_from_string(item_str))
 
def type_from_string(string):
    total = []
    for i in re_sub(',( )+',',',string).split():
        total.append(type(literal_eval(i)))
    return total

print(type_from_string('True     5 [5,  8] 1e+5'))




data_list = [1, "текст", True, 2.32, [1, 2, 3], 23, 54, {5, 4, 3, 2, 1}, "радио"]

for dict_key in data_list:
    func_dict_hash (dict_key)
    print ()



string = 'This is laughing laugh'

