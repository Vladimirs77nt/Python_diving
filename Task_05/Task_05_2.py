# Задача 2

# Самостоятельно сохраните в переменной строку текста.
# Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# Напишите преобразование в одну строку.

def func (str_):
    return {i: ord(i) for i in str_}

txt = "Гадкие лебеди"
print (func(txt))