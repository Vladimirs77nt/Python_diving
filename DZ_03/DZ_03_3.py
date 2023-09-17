# Задание №2

# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

# * Доп.задача: Верните все возможные варианты комплектации рюкзака.

import itertools

# функция расчета вес по списку вещей
def item_list_weight (list_item): # входной аргумент - список list
    global my_items
    weight = 0
    for i in list_item:             # перебираем список
        weight += my_items[i]
    return weight

# проверка на вхождение элементов списка list_1 в список list_2
#  * Точнее - является ли "множество 1" подмножеством "множества 2"
def list_entry (list_1, list_2): 
    for i in list_1:
        if i not in list_2:
            return False
    return True

# перебираем вещи по порядку входящего списка - слева направо, останавливаемся по достижении макс.веса
def counting_weight(list_, weight_max):
    global my_items
    list_items = []
    weight = 0
    for i in list_:
        if (weight + my_items[i]) > weight_max:
            continue
        weight += my_items[i]
        list_items.append(i)
    return list_items


############################################################################

my_items = {"палатка": 5.65,
            "спальник": 2.8,
            "коврик-пенка": 0.45,
            "набор посуды": 0.95,
            "котелок": 0.75,
            "консервы": 2.5,
            "рис/гречка": 2.1,
            "топорик": 0.65,
            "лопатка": 0.45,
            "фонарик": 1.05,
            "специи": 0.55,
            "тренона": 0.45,
            }
weight_max = 15             # максимальный вес рюкзака
lenght = len(my_items)      # кол-во вещей в словаре

print ()
print (f"Максимальный вес рюкзака: {weight_max}")
print (f"Список всех вещей для рюкзака:\n{my_items.keys()}")
print ()


print (" --- Вариант 1 (простой) ---")
set_items_1 = counting_weight(my_items, weight_max)
print (f"Итак, в рюкзак помещаем: {set_items_1}, суммарный вес: {round(item_list_weight((set_items_1)),2)}")


print ()
print (" --- Вариант 2 (перебор вариантов) ---")
count = 1
count_stop = 38         # максимальное возможное количество вариантов
common_list = []        # формируемый глобальный список вариантов набора вещей

print (">> подготовка списка вариантов... ждите!")

# используем функцию permutations() модуля itertools
for i_list in itertools.permutations(my_items, lenght): # список вещей с перестановками

    # берем из итератора часть вещей до достижения лимита веса 
    list_items = counting_weight(i_list, weight_max)
    # на выходе получаем вариант списка вещей

    # проверяем что список подобранных вещей НЕ входит в ГЛОБАЛЬНЫЙ список из подобранных вариантов
    if list_items in common_list: 
        continue

    f = False # булевый флаг - вдруг такая комбинация вещей уже была
    for i in common_list:
        if list_entry (list_items, i): # ну вот! такая комбинация вещей уже есть в списке вариантов
            f = True
            break
        if list_entry (i, list_items): # ага! такой вариант ЛУЧШЕ чем уже есть в списке вариантов
            common_list.remove(i)
            count -= 1
            break
    if f:
        continue
    common_list.append(list_items)
    print (f"{count} из {count_stop}")
    count += 1
    if count>count_stop:
        break

# длина самой длинной строки комплекта (для выравнивания с отступом)
len_max = len(max(list(map(lambda x: ', '.join(x), common_list)), key=len))

# печатаем список вариантов комплектации с форматированным видом
print ()
for count, i in enumerate(common_list, 1):
    regex = ', '.join(i)
    print (f"Вариант №{count:<3}-> {regex:.<{len_max+3}} суммарный вес: {round(item_list_weight(i),2)}")

print ()
print (" -- меняя значение count_stop в строке 72 - можно увеличить или уменьшить кол-во искомых вариаций комплектации")