#tuple - кортеж, list - список

# my_tuple = (1, 2, 3, "qwerty", True, None, "tuple") # неизменяемый объект
# my_list = [1, 2, 3, "qwerty", True, None, "list"] # изменяемый объект

# print(type(my_tuple), type(my_list))

######## итерируемые объекты ########

# print(my_tuple[2:])
# print(my_list[2:])

# new_tuple = tuple(my_list)
# print(new_tuple)
#
# new_list = list(my_tuple)
# print(new_list)

###############

# new_list = list()
# print(new_list)
#
# new_tuple = tuple()
# print(new_tuple)

# new_list = list('qwerty')
# print(new_list)

# new_tuple = tuple('qwerty')
# print(new_tuple)

# new_list = ['qwerty']
# print(new_list, type(new_list))
#
# new_tuple = ('qwerty') #круглые скобки не воспринимаются и получается строка
# print(new_tuple, type(new_tuple))
# new_tuple = ('qwerty', ) #если поставить запятую, то получается кортеж
# print(new_tuple, type(new_tuple))

# new_list = ['qwerty',
#             'qwer',
#             'qw',
#             ] # рекомендуемый вариант записи списков и кортежей

# my_new_list = [0, 2] * 4
# print(my_new_list)

# base_list = [1, 2, 3]
# new_list = [base_list] * 5
# print(new_list)

###################################

# my_tuple = (1, 2, 3, "qwerty", True, None, ["tuple"])
# my_list = [1, 2, 3, "qwerty", True, None, ["list"]]

# value = 10
# my_list[-1][0] = value
# print(my_list)

# value = 10
# my_tuple[-1][0] = value
# print(my_tuple)

# base_list = [1, 2, 3]
# my_new_list = base_list * 4
# print(my_new_list)
# base_list[0] = 10
# print(f"{base_list}")
# print(f"{my_new_list}")

# base_list = [1, 2, 3]
# my_new_list = [base_list.copy()] * 4
# print(my_new_list)
# base_list[0] = 10
# print(f"{base_list}")
# print(f"{my_new_list}")

##############################
# my_list = []
# if my_list:
#     value = my_list[0]
#     print(value)

# my_list = [1, 2, 3]
# index_value = 4
# value = 100
#
# if len(my_list) > index_value:
#     value = my_list[index_value]

# try:
#     value = my_list[index_value]
#
# except IndexError:
#     pass

# print(value)

##################################

# my_list = []
# my_str = 'qwerty'
# my_list.append(1) #метод добавления элемента в конец списка
# my_list = list(my_str)
# for symbol in my_str:
#     my_list.append(symbol)
#
# print(my_list)
#
# # my_list.pop() # метод удаления элемента с конца с писка
# new_el = my_list.pop() # pop возвращает элемент, который удаляет из списка
#
# print(my_list, new_el)

#########################################

# my_str = 'qwerty'
# my_list = list(my_str)
# print(my_list)
#
# new_str = ''.join(my_list)
# print(new_str)
# new_str = '.'.join(my_list)
# print(new_str)
# my_list = ['tmp', 'home', 'images', 'photo.png']
# new_str = '/'.join(my_list)
# print(new_str)

file_path = 'home/Users/Fantomas/Desktop/lesson.py'
parts = file_path.split('/')
print(parts)
parts[-1] = 'test.txt'
file_path = '/'.join(parts)
print(file_path)

############сортировка##############

# # my_list = [2, 5, 1, 9, -4, 7]
# my_list = ['tmp', 'A', 'home', 'images', 'photo.png', '1', '@', '[']
#
# # my_list.sort() #сортирует текущий список без возможности вернуть старый порядок
# # print(my_list)
#
# sort_list = sorted(my_list) # создает копию и ее сортирует
# print(sort_list)

#ASCII - таблица символов
# print(ord('A'), ord('@'), ord('['))
# print(chr(102))

# sort_list = sorted(my_list, reverse=True) # сортирует в обратном порядке
# print(sort_list)
#
# sort_list = sorted(my_list, key=len) # работа с ключами
# print(sort_list)