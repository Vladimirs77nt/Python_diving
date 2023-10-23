# Задание №1

# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_letters

def clear_text (text: str):
    result = ""
    for i in text:
        if i in ascii_letters + " ":
            result += i
    return result.lower ()

s = "EMGeg 29484 опщуощп ;lkjf;eef"
print (s)
print (clear_text (s))