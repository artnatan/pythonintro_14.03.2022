#модули

# import string

# alphabet = ''.join([chr(idx) for idx in range(ord('a'), ord('z') + 1)])

# alphabet = string.ascii_lowercase
# print(alphabet)

####################типы импорта###############
#1 var
# import string
#
# alphabet = string.ascii_lowercase
# print(alphabet)

#2 var
# from string import ascii_lowercase
#
# alphabet = ascii_lowercase
# print(alphabet)

#3 var

# from string import ascii_lowercase as alphabet
#
# print(alphabet)

#1 var
# import random
#
# value = random.randint(1, 10)
# print(value)
#
# my_cases = [True, False, 100, 'qwerty']
#
# case = random.choice(my_cases)
# print(case)
#
# my_str = 'qwerty'
#
# print(my_cases)

# 2var

from random import randint, choice
# value = randint(1, 10)
# print(value)
#
# my_cases = [True, False, 100, 'qwerty']
#
# case = choice(my_cases)
# print(case)

min_limit = -10
max_limit = 10

def print_point(point):
    print(f'({point["x"]}, {point["y"]}, {point["z"]})')

def create_point(min_limit, max_limit):
    point = {'x': randint(min_limit, max_limit),
              'y': randint(min_limit, max_limit),
              'z': randint(min_limit, max_limit),
              }
    return point

point_a = create_point(min_limit, max_limit)
point_b = create_point(5, 50)
point_c = create_point(-200, 30)

triangle_abc = (point_a, point_b, point_c)
print(triangle_abc)
print_point(point_a)