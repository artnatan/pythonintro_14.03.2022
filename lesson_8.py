# словари и методы словарей

my_dict = {"key": "value"}  # ключ - любой НЕИЗМЕНЯЕМЫЙ объект, значение - любой объект
print(my_dict, type(my_dict))

address = {"city": "Dnipro",
           "street": "Polya",
           "zip": 49000}

person = {"name": "John",
          "age": 24,
          "job": "president",
          "address": address
          }

print(person)
print(person["name"], person["age"], person["address"]["city"])
####################################################################################
test_dict = {1: "test_1", 2.3: "test_2", (1, 2): 1000, (tuple([1, 2]), 1): "test"}
print(test_dict[((1, 2), 1)])

from random import randint
cube_dict = {1: "this is 1",
             2: "this is 2",
             3: "this is 3",
             4: "this is 4",
             5: "this is 5",
             0: "this is 6",
             }
value = randint(1, 100)
my_result = cube_dict[value % 6]
print(value, my_result)
####################################################################################
test_dict = dict()
test_dict["new_key"] = 100
my_dict = {"test": "value", "new_key": 2}
test_dict.update(my_dict)

# get_value = test_dict["key"]
get_value = test_dict.get("key", -1)
pop_value = test_dict.pop("new_key")
test_dict["NEW_KEY"] = pop_value
print(pop_value, test_dict, get_value)
address["district"] = "center"
address["Zip"] = 49001
print(address)
##############################################################
# key = "key"
# if key in address:  # in смотрит в ключи!!!!
#     get_value = address[key]
#     print(get_value)
# else:
#     address[key] = None
#
# print(address.keys())
#
# for key in address:
#     print(key, address[key])
#
# values = list(address.values())
# values.append(5)
# print(values)
# for value in address.values():
#     print(value)
#
# items = address.items()
# print(items)
# for key, value in address.items():
#     print(value, key)
#
# ######################################################
#
# ascii_dict = {}
# for key in range(50, 100):
#     ascii_dict[key] = chr(key)
#
# ascii_dict = {key: chr(key) for key in range(50, 60)}
# print(ascii_dict)
#
# ascii_dict_values = {}
# for key, value in ascii_dict.items():
#     ascii_dict_values[value] = key
#
# print(ascii_dict_values)
#
# persons = {"Jones": 12, "Jackson": 12}
# result = {}
# for key, value in persons.items():
#     result[value] = key
#
# print(result)
#
# ####################################################################################
# price_list = [{"product": "MacBook", "price": 32000, "brand": "Apple"},
#               {"product": "MacBookPro", "price": 52000, "brand": "Apple"},
#               {"product": "HP", "price": 15000, "brand": "HP"}]
#
# prices = []
# for notebook in price_list:
#     prices.append(notebook["price"])
# average_price = sum(prices) / len(prices)
#
# print(average_price)
#
#
#
# # распаковка кортежей и списков
#
# my_tuple = (1, 2, "OK", "test", 200)
# value_1, value_2, my_str = my_tuple
# print(value_2, my_str)
# ######################################
# value_1 = 2
# value_2 = 4
# value_2, value_1 = value_1, value_2
# # объяснение процесса обмена значений переменных
# tmp = value_1, value_2
# print(tmp)
# value_2, value_1 = tmp
# print(value_1, value_2)
# ######################################
# value_1, _, _, my_str = my_tuple
# print(value_1, my_str)
#
# value_1, value_2, *_ = my_tuple
# print(_)
#
# print(my_tuple)
# print(*my_tuple)