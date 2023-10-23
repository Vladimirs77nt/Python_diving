# 4.2 Декоратор @property
# ● Setter

class User:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        return self._age
        
    @age.setter
    def age(self, value):
        if value > self._age:
            self._age = value
        else:
            raise ValueError(f'Новый возраст должен быть больше текущего: {self._age}')
            
        
            
user = User('Стивен', 'Спилберг')
print (user)
user.age = 75
print (user)
print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
print('Прошёл один год.')
user.age = 76
print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
print('Прошло несколько лет. Изобретена технология омоложения. Но возраст она не уменьшает.')
user.age = 25 # ValueError: Новый возраст должен быть больше текущего: 76