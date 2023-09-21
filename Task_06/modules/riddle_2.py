# модуль "отгадай загадку"

import random

def func_riddle_list ():
    # словарь загадок с ответами
    riddle_list = {
        "Не акула, а зубы имеет,\nПерекусить дерево сумеет,\nВ руки ты ее бери\nИ туда-сюда води.": ["Пила"],
        "Он старается упорно,\nЧтоб учёбу и работу\nПосещали мы бесспорно.\nНо корят его заботу.": ["Будильник"],
        "Сияют миллиарды созвездий, звезд, комет\nНа небосводе бархатном искрами золотыми.\nПришло время романтиков, мечтателей, поэтов,\nНо каково же будет для этой поры имя?": ["Ночь"],
        "Кто трудился — получи\nИ от радости кричи.\nОчень она славная,\nА размер — не главное!": ["Зарплата"],
        "Его вечно у нас нет,\nКуда девается — секрет,\nУтекает, как вода,\nНо не выйдет никогда!": ["Время"],
        }
    while riddle_list:
        riddle_c, answer_c = random.choice(list(riddle_list.items()))
        riddle_list.pop(riddle_c)
        yield [riddle_c, answer_c]
        
def func_ridde_game (riddle, answer, count_max):
    count = 0
    answer = list (map(lambda x: x.lower(), answer))
    print()
    print (f"Загадана загадка - отгадай ее не больше чем за {count_max} попыток (-ки)")
    print()
    print (riddle)
    print ()

    while True:
        count += 1
        print ("Попытка №", count)
        answer_input = input(f"Введите ответ: ")
        if answer_input.lower() in answer:
            print(">>> Ты отгадал загадку! за", count, "попыток (-ки)")
            print()
            return count
        else:
            print(">>> Ответ неверный!")
            print()
            if count == count_max:
                print()
                print("Ты проиграл! Попытки исчерпаны...")
                print("... а ответ на загадку такой:", answer)
                return 0
            print(">>> Попробуй еще!")
        print()
        if count > count_max:
            return 0
        
def game_start (count_lim):
    a = 0
    riddle_dict_gen = func_riddle_list()
    while True:
        try:
            riddle, answer = next (riddle_dict_gen)
            
            if a == 0:
                print ("----------------- Первая загадка! ----------------")
            else:
                print ("---------------- Следующая загадка ---------------")

            func_ridde_game (riddle, answer, count_lim)
            a += 1
        except StopIteration:
            print ("------------------- ИГРА ЗАВЕРШЕНА ! ------------------")
            break