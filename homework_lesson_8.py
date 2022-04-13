from statistics import mean

# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.

my_list = ['100', 'true', 'OK', 'test', '200', 'qwe']
new_list = []

for idx, symbol in enumerate(my_list):
    if idx % 2 == 0:
        new_list.append(symbol)
    else:
        new_list.append(symbol[::-1])

# for idx in range(len(my_list)):
#     if idx % 2 == 0:
#         new_list.append(my_list[idx])
#     else:
#         new_list.append(my_list[idx][::-1])
#
print(f'#1: {new_list}')

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".

my_list = ['a100', 'true', 'AOK', 'test', 'a200', 'qwe']
new_list = []

for symbol in my_list:
    if symbol[0] == 'a':
        new_list.append(symbol)
print(f'#2: {new_list}')

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ['100', 'tarue', 'OK', 'test', '200.a', 'qawe']
new_list = []

for symbol in my_list:
    if 'a' in symbol:
        new_list.append(symbol)
print(f'#3: {new_list}')

# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Создать список и поместить туда имя самого молодого человека. Если возраст совпадает - поместить все имена самых молодых.
# б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
# в) Посчитать среднее количество лет всех людей из начального списка.

persons = [{"name": "John", "age": 15},
           {"name": "Jack", "age": 45},
           {"name": "Jasy", "age": 25},
           {"name": "Jackson", "age": 90},
           {"name": "Jackil", "age": 15},
           ]
# а)
min_age = min(dic['age'] for dic in persons)
name_list_a = [dic['name'] for dic in persons if dic['age'] == min_age]
# б)
max_name_len = max(len(dic['name']) for dic in persons)
name_list_b = [dic['name'] for dic in persons if len(dic['name']) == max_name_len]
# в)
middle_age = mean(dic['age'] for dic in persons)

print(f'#4: а: {name_list_a}, \n    б: {name_list_b}, \n    в: {middle_age}')

# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

my_dict_1 = {1: 1,
             2: 2,
             '1': 'Goo',
             'street': 'first',
             }

my_dict_2 = {'1': 1,
             2: '2',
             'name': 'Jo',
             }
# а)
set_intersection = set(my_dict_1.keys()).intersection(set(my_dict_2.keys()))
list_a = list(set_intersection)
# б)
set_difference = set(my_dict_1.keys()).difference(set(my_dict_2.keys()))
list_b = list(set_difference)
# в)
new_dict = {}
for key in list_b:
    new_dict[key] = my_dict_1[key]
# # г)
union_dict = my_dict_1.copy()

for key, value in my_dict_2.items():
    if key in my_dict_1.keys():
        union_dict[key] = [my_dict_1[key], value] # не могу наверняка определить причину выделения [my_dict_1[key], value]...
    # Предполагаю, что такой синтаксис использует иной тип данных Union. Однако, проверял на типы данных type([my_dict_1[key], value]), определяет как список.
    # Код отрабатывает верно при существующих данных.
    else:
        union_dict[key] = value

print(f'#5: а: {list_a}, \n    б: {list_b}, \n    в: {new_dict}, \n    г: {union_dict}')
