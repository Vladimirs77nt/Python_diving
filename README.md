***Погружение в Python (семинары)***

Преподователь: Кирилл Панфилов

старт: 25.08.2023

-----------------------------------------------------

Урок 12. ООП Финал (03.10.23)

  Лекция - не просмотрена... ❌
  
  Семинар - не просмотрен... ❌

-----------------------------------------------------

Урок 11. ООП Особенности Python (29.09.23)

  Лекция - не просмотрена... ❌
  
  Семинар - не просмотрен... ❌

-----------------------------------------------------

Урок 10. ООП Начало (26.09.23)

  Лекция - не просмотрена... ❌
  
  Семинар - не просмотрен... ❌

-----------------------------------------------------

Урок 9. Декораторы (22.09.23)

  Лекция - сейчас на просмотре ✅
  
  Семинар - не просмотрен... ❌
  ...домашние задачи к семинару №9 - не решены... ❌

-----------------------------------------------------

Урок 8. Сериализация (19.09.23)

Домашняя задача к семинару №8 - решена (03.10.2023)

* Решить задачи, которые не успели решить на семинаре.

 - Все задачи мною решены, но по частично по своему - как я расшифровал текст задач и выбор ключей
   Смотри в папке Task_08

* Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle. 
○ Для дочерних объектов указывайте родительскую директорию. 
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

  - сделал 3 варианта решения, итог конечно наверное не совсем тот...
  - Первые два DZ_08_ver_1.py и DZ_08_ver_2.py - в общем полностью одинаковые, основаны на функции os.listdir(dir_path). Там только немного логика записи отчета разная. Используется рекурсивный вызов функции самой себя. Алгоритмы считают размер файлов и вложенных все правильно - проверял
  - Третий вариант DZ_08_ver_1.py использует функцию os.walk(dir_path), но что-то не учел... Подсчитывает только размер файлов в папке, без учета вложенных папок.


-----------------------------------------------------

Урок 7. Файлы и файловая система (15.09.23)

Домашние задачи к семинару №7 - все решены !!! (25.09.2023)

Задание №1.
* Решить задачи, которые не успели решить на семинаре.

  <<< ВНИМАНИЕ !!! >>>
  - Запись семинара №7 (Файлы и файловая система) обрывается на 1:12:15, т.е. записано меньше чем полурока...
    На записи видно решение только двух задач из семи...
  - Все задачи с 3 по 7 мною решены - находятся в папке Task_07

Задание №2. (файл "DZ_07_2.py" в папке "DZ_07")
* Напишите функцию группового переименования файлов.
 Она должна:
 - принимать параметр желаемое конечное имя файлов. при переименовании в конце имени добавляется порядковый номер.
 - принимать параметр количество цифр в порядковом номере.
 - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
 - принимать параметр расширение конечного файла.
 - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

  --- для решения задачи подготовил следующие функции:
  * init (_dir):           - инициализация рабочей папки (папка с файлами для переименования)
  * file_get_name_extesion (file_str):  - функция возвращает название файла (до последней точки) и расширение файла (кортеж)
  * rename_group (_exc_file_in, _exc_file_out, _origin_name_range [], _digit: int, _file_name_out=""): 
                                        - функция группового переименования файлов
 
3адание №3.
* Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

  --- в папке DZ_07 есть папка modules -  в ней файл file_module.py - это пакет со всеми функциями с семинара

-----------------------------------------------------

Урок 6. Модули

Решены домашние задачи к семинару №6 (21.09.2023) ✅

* Задача №1 (она же задача №7 с семинара №6 - про  дату)
(файл "DZ_06_1.py" в папке DZ_06 + модуль "time_module.py" в папке DZ_06/modules)

Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна. Для простоты договоримся, что год может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.

 --- в модуле "time_module.py" всего две функции:
     1. Функция data_check - основной модуль: сплитует входящую строку по точке, с помощью map переводит числа в int, проверяет вхождение года в диапозон 1...9999 и месяц в диапахон 1...12. Отдельной функцией определяет високосноть года и кол-во дней в феврале. Кол-во дней в каждом месяце определяю с помощью словаря, где ключ - номер месяца.
     2. Защищенная функция _check_leap_year - проверяет год на високосность


* Задача №2  (файл DZ-06-2.py в папке DZ-06)

В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

 --- Аргумент получаем через ys.argv:  

 --- Проверяем - не пустой ли аргумент. Если пустой то даем какое-то значение по умолчанию...

 --- вызываем функцию в модуле через контроль с исключением try/except (вдруг написали аргумент какую-то фигню...)


* Задача №3 (файл DZ-06-3.py в папке DZ-06 + модуль "chess.py" в папке DZ_06/modules)

Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

  --- для решения поствленных задач в модуле "chess.py" были созданы следующие функции:
  1) print_сhess_table(list_pairs): - функция печати шахматной доски 8х8 -> на входе список ферзей с координатами
  2) queens_list_random (): - функция формирования списка со случайной (рандомной) расстановкой 8 ферзей -> на ВЫХОДЕ список ферзей с координатами
  3) check_placement_queens_list (list_pairs): - функция определяет не бьют ли 8 ферзей из списка друг друга? -> True или False
     - эта функция сама многострочная - множество проверок по все возможные стороны движения ферзя
  4) _place_battle (_chess_board, x, y): - защищенная функция определения всех клеток, которые будут находится под ударом ферзя
  5) _placement_chess_table_list (list_pairs): - формирование доски 8х8 -> на входе список ферзей с координатами

* Задача №4

Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

  --- для решения в модуль chess.py была добавлена еще одна функция:
  * queens_list_random_8 (): - функция формирования списка c гарантированной расстановкой из 8 ферзей -> на ВЫХОДЕ получаем список ферзей с координатами
  --- Работа функции простая:
  1) обязательно формируем игоровое поле, где 0 - это свободное место, 1 - это ферзь, -1 - это место под ударом ферзя
  2) проходим в цикле с 0 по 7 ряд
  3) внутри ряда формируем список из 7 столбцов - предварительно перетасовав его случайно (random.shuffle)
  * в цикле проходим этот список каждый сверяясь с игровым полем
  * если клетка свободна - то ставим ферзя и заново пересчитываем игровое поле, находя новые клетки которые будут под ударом нового ферзя
  4) таким образом проходим все ряды. если после всех проходов получилось расставить все 8 ферззей - возвращаем список
  * если нет - начинаем все циклы заново

-----------------------------------------------------
Решены домашние задачи к семинару #5 (17.09.2023) ✅

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

  *yield ({name_[i]: (stavka_[i] * float(prem_[i][0:-1]) / 100) for i in range (len(name_))})*

* Задача №4  (файл DZ-05-4.py в папке DZ-05)
Создайте функцию генератор чисел Фибоначчи (см. Википедию).

--- Создаем функцию-генератор с возвратом по команде yield. Входных аргументов нет - работает до бесконечности
    В цикле проверка на старт - возвращает (yield) первые числа 0 и 1, а далее уже последужщие числа суммируются с предыдущими

* Задача №5  (файл Task-05-6.py в папке Task-05)
Задача №6 - "Таблица умножения" с семинара
*Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.*
*Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения.*
*Для вывода результата используйте «принт» без перехода на новую строку.*

--- Решение оказалось почти идентичным твоему, позже увиденному на экране записи семинара

    мой вариант:
  *print ("\n\n".join (["\n".join(["\t\t".join([f"{i+k} Х {j} = {(i+k)*j}" for k in range (0,4)]) for j in range (2,11)]) for i in [2,6]]))*

    твой вариант:
  *print ("\n\n".join(["\n".join(["\t\t".join([f"{x:^3}х{y:^3}= {x*y:^3}" for y in range (2+i, 6+i)]) for x in range (2, 11)]) for i in [0, 4]]))*

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