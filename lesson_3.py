# тип bool, none

# none_value = None
# print(none_value, type(none_value))

# value = 123
# id_value = id(value)
# print(id_value)
#
# print_value = print(value)
# print(print_value)

################################################

# value_1 = True
# value_2 = False
# print(type(value_1), type(value_2))

# bool_value = 4 > 2
# print(bool_value)
#
# bool_value_2 = 4 > 21
# print(bool_value_2)
#  <, >, >=, <=, ==, !=

# bool_value = 'qwe' in 'qwerty'
# print(bool_value)

##########################################

# value_int = 12
# value_float = 3.14
#
# result = value_float + value_int
# print(result)

# value_int = 1
#
# value_float = float(value_int) # int to float
# value_str = str(value_int) # int to str
# value_bool = bool(value_int) # int to bool.  True всегда, кроме нуля
#
# print(value_str, value_float, value_bool)
#############################################################

# value_float = 3.99
# value_int = int(value_float) # отрезание после точки

# value_str = '10'
# value_int = int(value_str)
# value_float= float(value_str)
# value_bool = bool(value_str)
#
# print(value_int, value_float, value_bool)

# value_str = 'qwe'
# value_bool = bool(value_str)
# print(value_bool * 2)

#############################################
# if

# value = 0
#
# if value > 0:
#     print(f'{value} больше 0')
# elif value == 0:
#     print(f'{value} равно 0')
# else:
#     print(print(f'{value} меньше 0'))

#################################################
# функция input

# input_value = input("введи число: ")
# input_value = int(input_value)
# if type(input_value) == int:
#     print(input_value)
# else:
#     print('ошибка')

###############################################

# input_value = input("введи число: ")
# try:
#     input_value = int(input_value)
#     print(input_value)
# except:
#     pass

###################обработка ошибок#########################
#
# input_value = input("введи число: ")
# try:
#     input_value = int(input_value)
#     print(input_value)
# except ValueError:
#     print('Введено не целое число')

########################домашка##############################

# input_case = input('Выбери тип операции: \n1 +\n2 -\n3 *\n4 /\n')
# value_1 = input("введи число: ")
# value_2 = input("введи число: ")


www = "www.conquer_and_command.net"

if ".com" in www:

    print("com in www")

else:

    print("com not in www")