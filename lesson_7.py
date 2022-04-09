
# my_str = 'blablacar'
# my_symbol = 'bla'
#
# result = my_str.count(my_symbol)
# print(result)

##############################################
# my_str = 'blablacar'
# my_symbol = 'bla'
#
# count = my_str.count(my_symbol)
# for _ in range(count):  # _ - имя переменной, которая не используется в коде дальше
#     print(my_symbol)

##############################################
# my_str = 'bla BLA car'
# my_str = my_str.lower()
# box = []
#
# for symbol in my_str:
#     if symbol not in box:
#         box.append(symbol)
# result = len(box)
# print(result)

##############################################
# my_str = "dfhourhfaounvjlnC?N"
# my_list = []

# print(id(my_list))

# my_list.extend(list(my_str[::2]))
#
# for index, symbol in enumerate(my_str):
#     if not index % 2:
#         my_list.append(symbol)
# #
# for symbol in my_str[::2]:
#     my_list.append(symbol)
# print(my_list, id(my_list))

################################################
# my_str = "qwertyuiop"
# str_index = [0, 9, 9, 1, 5]
# my_list = []
#
# for index in str_index:
#     value = my_str[index]
#     my_list.append(value)
# print(my_list)

###############################################
# my_int = 12345678456214512
# result = len(str(my_int))
# print(result)

# result = max(str(my_int))
# print(result)

# result = int(str(my_int)[::-1])
# print(result)

#####################################
# my_list_1 = [1, 2, 3, 4, 5]
# my_list_2 = [10, 20, 30, 40]
# my_result = []
#
# list_len = len(my_list_1)
# for index in range(list_len):
#     value_1 = my_list_1[index]
#     value_2 = my_list_2[index]
#     my_result += [value_1, value_2]
#
# my_result += my_list_1[list_len:]
# my_result += my_list_2[list_len:]
# print(my_result)

#генератор списков
# my_str = "qwerty"
# my_list = []
# for symbol in my_str:
#     my_list.append(symbol)
# my_list =[symbol for symbol in my_str]
# print(my_list)

# limit_value = 5
# numbers = [number for number in range(limit_value)]
# print(numbers)

# my_list = [12, 34, -54, 2, -6, 8]
#
# result = [value for value in my_list if value > 0]
# print(result)

# alphabet = [chr(index) for index in range(ord('a'), ord('z')+1)]
# print(alphabet)

##########################################################
#множества

# my_list = list('qwerty123ytrewq321')
# my_set = set(my_list) # нет повторов, нет четкого порядка, неизменяемый
# print(my_set, type(my_set))

# my_str = 'bla BLA car'
# my_str = my_str.lower()
# result = len(set(my_str))
# print(result)

# my_list = [1, 2, 3, 2, 2, 3]
# print(set(my_list))

my_set_1 = set('12345')
my_set_2 = {"1", "2", 3}
print(my_set_2, my_set_1)

result_union = my_set_1.union((my_set_2))
result_intersection = my_set_1.intersection((my_set_2))
result_difference = my_set_1.difference((my_set_2))
print(result_union, result_intersection, result_difference)

# my_str = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqa"
# for symbol in set(my_str):
#     print(symbol)