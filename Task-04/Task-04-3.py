# Задание №3

# ✔ Функция получает на вход строку из двух чисел через пробел. 
# ✔ Сформируйте словарь, где ключом будет символ из Unicode, а значением —  целое число. 
# ✔ Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

def dict_unicode (text):
    num_1 = int(text.split()[0])
    num_2 = int(text.split()[1])
    if num_2 < num_1:
        num_1, num_2 = num_2, num_1
    dict_unicode = {}
    for i in range (num_1, num_2+1):
        dict_unicode[chr(i)] = i
    return dict_unicode

num_str = "66 100"
print(dict_unicode(num_str))