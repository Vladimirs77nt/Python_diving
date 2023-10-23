from random import randint


def get_data():
    if result := randint (0, 3):
        return result
    else:
        raise ConnectionError

MAX_COUNT = 5
count = 0

while count < MAX_COUNT:
    count += 1
    try:
        data = get_data()
        break
    except ConnectionError as e:
        print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')

print (data)