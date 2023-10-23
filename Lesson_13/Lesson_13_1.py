def get(text: str = None) -> int:
    while True:
        try:
            num = int(input(text))
            break
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'f'Попробуйте снова')
    return num


number = get('Введите целый делитель: ')
print(f'100 / {number} = {100 / number}')