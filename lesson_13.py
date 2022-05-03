#  ООП
#  класс
#  экземпляр класса - self
#  атрибут класса
#  атрибут экземпляра класса
from typing import Optional


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.name_uppercase = self.get_name_uppercase()

    def __str__(self):
        return f'I am {self.name}. I am {self.age}'

    def __repr__(self):
        return f'I am {self.name_uppercase}. I am {self.age}'

    def increase_age(self):
        self.age += 1

    def get_name_uppercase(self):
        name_uppercase = self.name.upper()
        return name_uppercase


my_name = 'Artem'
my_age = 34
natan = Person(my_name, my_age)

person_1 = Person(name='Jhon', age=23)
person_2 = Person(name='Eva', age=23)
print(person_1.name, person_1.age)
print(natan)

person_1.increase_age()


persons = [person_1, person_2]
print(persons)

# class Person:  # класс
#     name: Optional[str] = None  # атрибут класса
#     age: Optional[int] = 0
#
#
# person_1 = Person()  # экземпляр класса (представитель объекта)
# person_2 = Person()
# person_3 = Person()
#
# person_1.name = 'Jhon'  # атрибут экземпляра класса
# person_1.age = 9
#
# person_2.name = 'Anna'
# person_2.age = 30
# person_2.gender = 'female'  #добавили атрибут в экземпляр класса
# Person.age = None
#
# print(person_1.name, person_1.age)
# print(person_2.name, person_2.age, person_2.gender)
# print(person_3.name, person_3.age)
