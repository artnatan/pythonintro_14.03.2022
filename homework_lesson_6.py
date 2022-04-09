# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

my_list = [1, 2, 4, 6, 7, 9, 100, 130, 150, 200]

for symbol in my_list:
    if symbol > 100:
        print(symbol)

#в одну строку
# [print(symbol) for symbol in my_list if symbol > 100]

# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

my_list = [1, 2, 4, 6, 7, 9, 100, 130, 150, 200]
my_results = []
for symbol in my_list:
    if symbol > 100:
        my_results.append(symbol)
print(my_results)
#в одну строку
# print([symbol for symbol in my_list if symbol > 100])


# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

my_list = [1, 2, 4, 6, 7, 9, 100, 130, 150, 200]
list_len = len(my_list)
if list_len < 2:
    my_list.append(0)
else:
    value_1 = my_list[list_len - 1]
    value_2 = my_list[list_len - 2]
    my_list.append(value_1 + value_2)

# в одну строку
# my_list.append(0) if len(my_list) < 2 else my_list.append(my_list[len(my_list) - 1] + my_list[len(my_list) - 2])
print(my_list)
