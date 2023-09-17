# Задание №8

# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.

# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

friends_dict = {}
friends_dict ["Иван"] = ("палатка", "топорик", "спальный мешок")
friends_dict ["Василий"] = ("котелок", "еда", "спальный мешок")
friends_dict ["Дмитрий"] = ("фонарик", "еда", "спальный мешок")
print ()

print (">>> Какие вещи взяли три друга (индивидуально)")
for name, items in friends_dict.items():
    items_str = ', '.join(items)
    print(f"{name} взял с собой: {items_str}")
print ()

print (">>> Какие вещи взяли все три друга (одинаково)")
for count, value in enumerate(friends_dict.items()):
    if count == 0:
        set_all = set(value[1])
    else:
        set_all = set_all.intersection(set(value[1]))
print(set_all)
print ()

print (">>> Какие вещи уникальны, есть только у одного друга")
friends_dict_2 = {}
set_other = ()
for count, value in enumerate(friends_dict.items()):
    counter = 0
    for count_other, value_other in enumerate(friends_dict.items()):
        if count == count_other:
            continue
        if counter == 0:
            set_all_other = set(value_other[1])
        else:
            set_all_other = set_all_other.union(set(value_other[1]))
        counter += 1
    # на выходе = set_all_other - список вещей, которые есть у всех остальных, множество!
    set_unique = set(value[1]) - set_all_other
    # на выходе РАЗНИЦА ДВУХ МНОЖЕСТВ
    print(f"{value[0]}: {set_unique}")

    # сразу формируем словарь вещей (имя ключ) которые есть у всех кроме одного
    friends_dict_2 [value[0]] = tuple (set(friends_dict[value[0]]) - set_unique - set_all)
    set_other += friends_dict_2 [value[0]]
print ()

print (">>> Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует")
name_other = ""
for name, items in friends_dict_2.items():
    if items == ():
        name_none = name
    else:
        name_other += name + " "
    items_str = ', '.join(items)

print (f"У друзей {name_other}есть {items_str}, а у {name_none} этого нет...")
print ()