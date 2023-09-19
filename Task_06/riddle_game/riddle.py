# модуль "отгадай загадку"

def func_ridde (riddle, answer, count_max):
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