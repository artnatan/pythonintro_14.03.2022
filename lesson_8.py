#распаковка кортежей и списков

# my_tuple = (1, 2, 'OK', 'test', 200)
# value_1, value_2, my_str = my_tuple
#
# print(value_2, my_str)

# value_1 = 2
# value_2 = 4

# value_2, value_1 = value_1, value_2
# print(value_1, value_2) #автоматически создает кортеж, так как ниже

# tmp = value_1, value_2
# value_2, value_1 = tmp
# print(tmp) #то же самое что и выше

#############################################################
# value_1, value_2, _, _ = my_tuple
# print(value_1, value_2)

# value_1, value_2, *_, last_value = my_tuple # * создает список
# print(last_value)

# print(my_tuple)
# print(*my_tuple)



######################словари и методы словарей##########################

# my_dict = {'key': 'value'} # ключ - любой НЕИЗМЕНЯЕМЫЙ объект, значение - любой объект
# print(my_dict, type(my_dict))

# address = {'city': 'Dnipro',
#            'street': 'Polya',
#            'zip': 49000,
#            }
#
# person = {"name": "John",
#           "age": 24,
#           "job": "president",
#           "address": address
#           }
#
# print(person['name'], person['age'], person['address']['city'])
# print(person)

# test_dict = {1: 'test_1',
#              2.3: 'test_2',
#              (1, 2): 1000,
#              }
#
# print(test_dict[(1, 2)])

# from random import randint
#
# cube_dict = {1: 'this is 1',
#              2: 'this is 2',
#              3: 'this is 3',
#              4: 'this is 4',
#              5: 'this is 5',
#              0: 'this is 6',
#              }
#
# value = randint(1, 100)
# my_result = cube_dict[value % 6]
# print(value, my_result)

# person = {"name": "John",
#           "age": 24,
#           "job": "president",
#           }
#
# test_dict = dict()
# test_dict['new_key'] = 100
# print(test_dict)
#
# person['hight'] = 120 # добавлять значение и ключ
# person['age'] = 12 # заменять значения по ключу
# print(person['hight'], person['age'])
#
# test_dict.update({'test': 'value'}) # обновление словаря другим словарарем
# get_value = test_dict.get('new_key') #получить значение по ключу
# get_value = test_dict.get('key', -1) #возвращает указанное значение, если такого ключа нет
# test_dict.pop('test') #удаляет по ключу
# print(test_dict, get_value)


###################################################################

address = {'city': 'Dnipro',
           'street': 'Polya',
           'zip': 49000,
           }

# key = 'key'
# if key in address: # in смотрит в ключи словаря
#     get_value = address[key]
#     print(get_value)
#
# print(address.keys())
#
# print(address.values())
#
# values = list(address.values())
# values.append(5)
# print(values)
#
# for value in address.values():
#     print(value)

# items = address.items()
# print(items)
#
# for key, value in address.items():
#      print(value, key)

################################################################

# ascii_dict = {}

# for key in range(50, 100):
#     ascii_dict[key] = chr(key)

# ascii_dict = {key:chr(key) for key in range(50, 60)}
# print(ascii_dict)
#
# ascii_dict_values = {}
# for key, value in ascii_dict.items():
#     ascii_dict_values[value] = key
# print(ascii_dict_values)


#############################################################

# persons = {'Jones': 12, 'Jacson': 12}
#
# result = {}
#
# for key, value in persons.items():
#     result[value] = key
#
# print(result)

########################################################

