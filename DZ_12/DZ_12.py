# Создайте класс студента.

# 📌 Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Если ФИО не соответствует условию, выведите: "ФИО должно состоять только из букв и начинаться с заглавной буквы"

# 📌 Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# Если такого предмета нет, выведите: "Предмет {Название предмета} не найден"

# 📌 Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# В противном случае выведите: "Оценка должна быть целым числом от 2 до 5"
# Результат теста должен быть целым числом от 0 до 100

# 📌 Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам
# всех предметов вместе взятых.

# Вам предоставлен файл subjects.csv, содержащий предметы.
# Сейчас в файл записана следующая информация: Математика,Физика,История,Литература
# Создайте класс Student, который будет представлять студента и его успехи по предметам.

# Класс должен иметь следующие методы:

# Атрибуты класса:
    # name (str): ФИО студента
    # subjects (dict): Словарь, который хранит предметы в качестве ключей и информацию об оценках и
    #                  результатах тестов для каждого предмета в виде словаря.

# Магические методы (Dunder-методы):
    # __init__(self, name, subjects_file): Конструктор класса. Принимает имя студента и файл с предметами и их
    #                                      результатами. Инициализирует атрибуты name и subjects и вызывает метод
    #                                      load_subjects для загрузки предметов из файла.
    # __setattr__(self, name, value): Дескриптор, который проверяет установку атрибута name.
    #                                 Убеждается, что name начинается с заглавной буквы и состоит только из букв.
    # __getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их
    #                          именам.
    # __str__(self): Возвращает строковое представление студента, включая имя и список предметов.

# Методы класса:
    # load_subjects(self, subjects_file): Загружает предметы из файла CSV. Использует модуль csv для чтения данных
    #                                     из файла и добавляет предметы в атрибут subjects.
    # add_grade(self, subject, grade): Добавляет оценку по заданному предмету.
    #                                  Убеждается, что оценка является целым числом от 2 до 5.
    # add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету.
    #                                            Убеждается, что результат теста является целым числом от 0 до 100.
    # get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.
    # get_average_grade(self): Возвращает средний балл по всем предметам.


import csv
import statistics


class Range_FIO:

    def __init__(self):
        pass

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, text):
        self.validate(text)
        setattr(instance, self.param_name, text)
    
    def validate(self, text):
        for i in text.split():
            if not (i.isalpha() and i.istitle()):
                raise ValueError ("ФИО должно состоять только из букв и начинаться с заглавной буквы")

class Student:

    name = Range_FIO()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = self.load_subjects (subjects_file)
    
    def load_subjects (self, subjects_file) -> dict:
        subjects_dict = {}
        with open (subjects_file, "r", encoding='utf-8') as f:
            csv_data = csv.reader (f, dialect="excel", delimiter=",")
            for i in csv_data:
                for k in i:
                    subjects_dict[k] = {"grade": [], "test_score": []}
        return subjects_dict
    
    def add_grade(self, subject, grade):
        if subject in self.subjects:
            if not isinstance (grade, int) or grade>5 or grade<2:
                raise ValueError (f"Оценка должна быть целым числом от 2 до 5")
            item = self.subjects.get (subject)
            self.subjects[subject]['grade'].append (grade)
            item_grade = item.get ('grade')
        else:
            raise ValueError (f"Предмет {subject} не найден")
        
    def add_test_score(self, subject, test_score):
        if subject in self.subjects:
            if not isinstance (test_score, int) or test_score>100 or test_score<0:
                raise ValueError (f"Результат теста должен быть целым числом от 0 до 100")
            self.subjects[subject]['test_score'].append (test_score)
        else:
            raise ValueError (f"Предмет {subject} не найден")
        
    def get_average_grade(self):
        average = 0
        count = 0
        for subject in self.subjects:
            item = self.subjects.get(subject)["grade"]
            if item == []:
                continue
            average += statistics.mean (item)
            count += 1
        return float(round ((average/count), 1))
    
    def get_average_test_score(self, subject):
        if subject in self.subjects:
            item = self.subjects.get(subject)["test_score"]
            if item == []:
                return None
            return float(round(statistics.mean (item), 1))
        else:
            raise ValueError (f"Предмет {subject} не найден")
        
    def __str__(self):
        subjects = ""
        for subject, item in self.subjects.items():
            item_geade = item["grade"]
            item_test_score = item["test_score"]
            if item_geade == [] and item_test_score == []:
                continue
            subjects += subject + ", "
        subjects = subjects[:-2]
        return f'Студент: {self.name}\nПредметы: {subjects}'

    def __repr__(self):
        return f'Student(name={self.name}, age={self.age}, grade={self.grade}, office={self.office})'


# ----------------------------------------


student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)