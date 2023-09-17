# Задание №2

# ✔ Напишите функцию, которая принимает строку текста. 
# ✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

def function (text):
    set_symbol = set()
    for c in text:
        set_symbol.add(ord(c))
    list_symbol = sorted(list(set_symbol), reverse=True)
    print (list_symbol)

text = "Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки. яяяяяяяяяяяяяяяяяяя"

# Вариант 1 - через функцию
function (text)

# Вариант 2 - через list comprehension
print ([ord(i) for i in sorted(list(set(text)), reverse=True)])