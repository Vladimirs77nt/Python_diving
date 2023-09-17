# Задача 3

# Продолжаем развивать задачу 2
# Возьмите словарь, который вы получили. Сохраните его итераторатор.
# Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

def func (str_):
    return {i: ord(i) for i in str_}

txt = "Гадкие лебеди"
txt_dict= func(txt)
print (txt_dict)

txt_iter = iter(txt_dict.items())
print ([next(txt_iter) for i in range(5)])