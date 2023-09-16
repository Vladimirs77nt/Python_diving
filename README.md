***Погружение в Python (семинары)***

Преподователь: Кирилл Панфилов

старт: 25.08.2023

-----------------------------------------------------
...домашние задачи к семинару №6 - не решены... ❌

  Лекция и семинар - не просмотрены ❌

-----------------------------------------------------
...домашние задачи к семинару №5 (14.09.2023) ✅ - в процессе

* Задача №1  (файл DZ-05-1.py в папке DZ-05)
Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2. 
Для проверки числа на простоту используйте правило:
«число является простым, если делится нацело только на единицу и на себя».

--- Создаем функцию-генератор с возвратом по команде yield. Входных аргументов нет - работает до бесконечности
    Впервые попоробовал интересную связку FOR - BREAK - ELSE, неожиданная возможность избавится от лишней переменной...

* Задача №2  (файл DZ-05-2.py в папке DZ-05)
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

--- Входящую строку для начала сплитим по слэшу (\), а затем для решения воспользуемся распаковкой коллекции в резиновые переменные (переменные со звездокой). Далле нужное опять джойним и выводим результат.  

* Задача №3  (файл DZ-05-3.py в папке DZ-05)
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида «10.25%».
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии

--- Для решения просто взято однострочное решение с семинара и возвращаемый словарь завернут в круглые скобки - для создания генератора. Возврат сделан также с помощью команды yield: 

    yield ({name_[i]: (stavka_[i] * float(prem_[i][0:-1]) / 100) for i in range (len(name_))})

* Задача №4  (файл DZ-05-4.py в папке DZ-05)
Создайте функцию генератор чисел Фибоначчи (см. Википедию).

--- Создаем функцию-генератор с возвратом по команде yield. Входных аргументов нет - работает до бесконечности
    В цикле проверка на старт - возвращает (yield) первые числа 0 и 1, а далее уже последужщие числа суммируются с предыдущими


-----------------------------------------------------
Решены домашние задачи к семинару №4 (14.09.2023) ✅

* Задача №1  (файл DZ-04-1.py в папке DZ-04)
Напишите функцию для транспонирования матрицы

--- Решение с помощью двух вложенных циклов for для перестановки индексов столбцов и строк:

    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

* Задача №2  (файл DZ-04-2.py в папке DZ-04)
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.

--- Решение с помощью цикла for для перебора входящих значений и проверки на хэшируемость (value.__hash__):

    return {value if value.__hash__ is not None else str(value):key for key, value in args.items()}

* Задача №3  (файл DZ-04-3.py в папке DZ-04)
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.

--- Решение - разбил на модули-функции:

- def init ():                                  # инициализация глобальных переменных и начальных данных
- def view_menu ():                             # вывод списка меню
- def view_cash ():                             # функция вывода текущего баланса
- def controller ():                            # основной модуль для выбора пункта меню и выполнения выбранной операции
- def amount_selecrion ():                      # ввод суммы на операцию снять/положить
- def accrual_of_money_interest (proc):         # функция начисления процента
- def operation_wealth_tax (tax, wealth_limit): # функция снятия налога на богатство

-----------------------------------------------------
Решены домашние задачи к семинару №3 (10.09.2023) ✅

* Решить задачи, которые не успели решить на семинаре.
  Это задача №8 - про друзей и поход (файл Task-03-8.py в папке Task-03)

-- Решена с помощью циклов и работы с множествами - пересечение, объединение, разница

* Задача №1  (файл DZ-03-1.py в папке DZ-03)
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

-- Решена с помощью словаря, где ключ - это значение элемента, а значение словаря - это кол-во повторов

* Задача №2  (файл DZ-03-2.py в папке DZ-03)
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

-- Решена с помощью словаря, где ключ - это "слово", а значение словаря - это кол-во повторов этого слова
-- с помощью ".lower()" - все буквы в нижний регистр
-- с помощью "re.sub" - убираю знаки пунктуации, кавычки
-- с помощью "join" - убираю лишние пробелы
-- и только после всего этого - текст сплитую

* Задача №3 (файл DZ-03-3.py в папке DZ-03)
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
* Верните все возможные варианты комплектации рюкзака.

-- Решена
-- Для решения использовал функцию permutations() модуля itertools - возвращает итератор с последовательными перестановками из элементов входной последовательности.
-- Опять же - возможно громозкое решение, но оно работет для любых комбинаций и любого кол-ва вариантов

-----------------------------------------------------
Решены домашние задачи к семинару №2 (03.09.2023) ✅

* Задача №1 (файл DZ-02-1.py в папке DZ-02)
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.

-- для решения использовал решенную задачу №3 с семинара для вычисления двоичного и восьмеринчого представления
т.к. логика решения единая для любой системы - использовал только дополнение - подстановку латинских букв из таблицы ASCII
по факту программа возвращает двоичное, восьмеричное и шеснадцатеричное представление введеного числа

* Задача №2 (файл DZ-02-2.py в папке DZ-02)
Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение дробей.
Для проверки своего кода используйте модуль fractions.

-- программа возможно получилась громозкой - но свою задачу выполняет
-- не удержался от использования функций def

-----------------------------------------------------
Решены домашние задачи к семинару №1 (28.08.2023) ✅

* Task-01-09 (Задача с семинара файл Task-01-09.py в папке Task-01)
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

* Задача №1 (файл DZ-01-1.py в папке DZ-01)
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c — стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с
суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника 
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, 
равнобедренным или равносторонним.

* Задача №2 (файл DZ-01-2.py в папке DZ-01)
Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу и на себя».
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

* Задача №3 (файл DZ-01-3 ver1.py в папке DZ-01)
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать «больше» или «меньше» после каждой попытки.

* Задача №3 версия 2 (файл DZ-01-3 ver2.py в папке DZ-01)
Пользователь загадывает число от 0 до 1000. Компьютер пытается его угадать (вычисляет) за 10 попыток.
...Зараза - всегда побеждает! кроме одного числа...