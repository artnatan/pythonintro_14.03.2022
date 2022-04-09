# 1. Дано целое число (int). Определить сколько нулей в этом числе.

my_int = 10002000
my_str = str(my_int)
print(f"#1:{my_str.count('0')}")


# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля

my_int = 1000200000
my_str = str(my_int)[::-1]
index = 0
my_list = []
while my_str[index] == '0':
    my_list.append(0)
    index += 1

print(f'#2:{len(my_list)}')


# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1 = ['q', 'w', 'e', 'r', 't', 'y']
my_list_2 = [1, 2, 3, 4, 5]
my_result = []

for symbol in my_list_1[::2]:
    my_result.append(symbol)
for symbol in my_list_2[1::2]:
    my_result.append(symbol)
print(f'#3:{my_result}')

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list = ['q', 'w', 'e', 'r', 't', 'y']
my_str = ''.join(my_list[1:]) + my_list[0]
new_list = list(my_str)
print(f'#4:{my_list}, {new_list}')

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list = ['q', 'w', 'e', 'r', 't', 'y']
pop_value = my_list.pop(0)
my_list.append(pop_value)
print(f'#5:{my_list}')

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)

my_str = "43 больше чем 34 но меньше чем 56"
result_list = my_str.split(' ')
result = 0
for symbol in result_list:
    if symbol.isdigit():
        result += int(symbol)
print(f'#6:{result}')


# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "sss My very long string yyy"
l_limit = "y"
r_limit = "s"
slice_list = [my_str.find('y'), my_str.rfind('s')]

sub_str = my_str[slice_list[0]+1: slice_list[1]]
print(f'#7:{sub_str}')

# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)

my_str = "Mylongstring!"
pair_list = []

if len(my_str) % 2 != 0:
    my_str += '_'

for str_i in range(0, len(my_str), 2):
    pair_list.append(my_str[str_i: str_i + 2])

print(f'#8:{pair_list}')

# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

my_list = [2, 4, 1, 5, 3, 9, 0, 5, 2]
new_list = []
count = 0

for _ in range(len(my_list)-2):#-2 так как крайние числа не учитываются, поскольку у них недостаточно соседей
    new_list.append(my_list[:3])
    my_list.pop(0)

for list_i in new_list:
    if list_i[1] > list_i[0] + list_i[2]:
        count += 1

print(f'#9:{count}')
# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.

my_list = [1, 2, "2", 3, "11", "22", 33]
result_list = []
for symbol in my_list:
    if type(symbol) == str:
        result_list.append(symbol)
print(f'#10:{result_list}')

# 11. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.

my_str = 'qwertyqwer112'
my_list = []

for symbol in my_str:
    if my_str.count(symbol) == 1:
        my_list.append(symbol)
print(f'#11:{my_list}')

# 12. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str_1 = '12345qwerty'
my_str_2 = '12_ui_tyy'
set_intersection = set(my_str_1).intersection(my_str_2)
my_list = list(set_intersection)

print(f'#12:{my_list}')

# 13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу

my_str_1 = 'eaaaasdf1'
my_str_2 = 'asdfff2bbbbbe'

my_list_1 = []
my_list_2 = []
my_result = []

for symbol in my_str_1:
    if my_str_1.count(symbol) == 1:
        my_list_1.append(symbol)
for symbol in my_str_2:
    if my_str_2.count(symbol) == 1:
        my_list_2.append(symbol)

my_result = list(set(my_list_1).intersection(my_list_2))

print(f'#13:{my_result}')
