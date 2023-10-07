# Задание №4

# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь


from sympy import summation
from Task_10_3 import People

class Worker (People):
    def __init__(self, last_name, first_name, patronymic, age, w_id, w_level):
        super().__init__(last_name, first_name, patronymic, age)
        self.w_id = w_id
        self.w_level = sum(lambda x: int(x) in str(w_id))//7

    def show_worker (self):
        return self.last_name + " " + self.first_name + " " + self.patronymic + " " + str(id) + " " + str (w_level)