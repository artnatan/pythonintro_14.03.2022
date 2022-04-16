from random import randint, choice
from string import ascii_lowercase

# Для задания 1-7 за основу можете взять код из предідущих ДЗ.
#
# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

my_list = ['a100', 'true', 'OK', 'test', 'a200', 'qawe']


def get_list_revers_str(list_str):
    new_list = list_str.copy()
    for index in range(len(list_str)):
        if index % 2:
            new_list[index] = list_str[index][::-1]
    return new_list


print(f'1: {get_list_revers_str(my_list)}')
# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".


def get_list_first_symbol(list_str):
    new_list = [value for value in list_str if value[0] == 'a']
    return new_list


print(f'2: {get_list_first_symbol(my_list)}')
# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.


def get_list_a_symbol(list_str):
    new_list = [value for value in list_str if 'a' in value]
    return new_list


print(f'3: {get_list_a_symbol(my_list)}')

# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.
my_list = [1, 2, "2", 3, "11", "22", 33]


def get_list_only_str(list_values):
    list_str = [value for value in list_values if type(value) == str]
    return list_str


print(f'4: {get_list_only_str(my_list)}')
# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.
my_str = 'qwertyqwer112'


def get_list_single_symbol(string):
    list_values = [symbol for symbol in set(string) if string.count(symbol) == 1]
    return list_values


print(f'5: {get_list_single_symbol(my_str)}')

# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str_1 = '12345qwerty'
my_str_2 = '12_ui_tyy'


def get_list_intersection(string_1, string_2):
    set_intersection = set(string_1).intersection(string_2)
    result_list = list(set_intersection)
    return result_list


print(f'6: {get_list_intersection(my_str_1, my_str_2)}')

# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.


def get_list_result(string_1, string_2):
    set_intersection = set(string_1).intersection(string_2)
    result_list = [value for value in set_intersection if string_1.count(value) == 1 and string_2.count(value) == 1]
    return result_list


print(f'7: {get_list_result(my_str_1, my_str_2)}')

# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.

names = ["king", "miller", "kean", "smith"]
domains = ["net", "com", "ua"]


def create_email(mail_domains, mail_names):
    alphabet = ascii_lowercase
    position_before_at = choice(mail_names) + '.' + str(randint(100, 999))
    position_after_at = [choice(alphabet) for _ in range(0, randint(5, 7))]
    domain = choice(mail_domains)
    e_mail_name = position_before_at + '@' + ''.join(position_after_at) + '.' + domain
    return e_mail_name


e_mail = create_email(domains, names)
print(f'8: {e_mail}')

# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com

