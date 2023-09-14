# Задание №2

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def func(**args):
    return {value if value.__hash__ is not None else str(value):key for key, value in args.items()}
# for key, value in args.items() - перебираем все входящие значения
# # value.__hash__ is not None - выражение проверки ключа на хэшируемость
# else str(value):key        - если ключ не хэшируемый - то переводим его в строкое представление

print (func (num = 542, txt = "текст", flag = True))
print (func (list_data = [1, 2, 3, 4, 5]))
print (func (dict_data = {1:"один", 2:2.0, 3:None}))
print (func (null_var = None, empty_data = []))
print (func (s1 = 23, s2 = 23, s3 = 23))