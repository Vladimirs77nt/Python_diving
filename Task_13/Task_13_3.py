# Задача №3

# Создайте класс с базовым исключением и дочерние классы исключения:
# 📌 ошибка уровня
# 📌 ошибка доступа

class UserException(Exception):
    def __init__ (self, msg):
        self.message = msg

    def __str__ (self):
        return f"Мое исключение: {self.message}"

class UserAccessException(UserException):
    def __init__ (self, msg): 
        super(UserAccessException, self).__init__(msg)

class UserLevelException (UserException):
    def __init__ (self, msg): 
        super(UserLevelException, self).__init__(msg)

raise UserAccessException ("Уровень доступа меньше чем 7")
