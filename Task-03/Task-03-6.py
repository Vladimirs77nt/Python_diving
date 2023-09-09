# Задание №6

# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
#   слова был один пробел между ним и номером строки.

text = input("Введите текст:")
text_lst = text.split()
text_lst.sort()
len_max = len(max(text_lst, key=len))
for i, j in enumerate (text_lst):
    print(f"{i+1} {j:>{len_max}}")