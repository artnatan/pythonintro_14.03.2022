import os
from string import ascii_lowercase as alphabet
from random import shuffle


def create_dir(dirname):
    os.makedirs(dirname, exist_ok=True)

def create_file(dirname, symbol):
    file_path = os.path.join(dirname,f'{symbol}.txt')
    with open(file_path, 'w') as txt_file:
        txt_file.write(alphabet.replace(symbol, symbol.upper()))

def create_files(dirname):
    for symbol in alphabet:
        create_file(dirname, symbol)

def do_tannos_click(dirname):
    dir_list = os.listdir(dirname)
    shuffle(dir_list)
    for filename in dir_list[::2]:
        os.remove(os.path.join(dirname, filename))

dirname = 'alphabet'
create_dir(dirname)
create_files(dirname)
do_tannos_click(dirname)


# параметры по умолчанию
# типы переменных
# импорт функций
# модуль os
# from utils.Files import read_txt_file
# import os
#
# path = 'utils'
# list_dir = os.listdir(path)
# print(list_dir)
#
# filename = 'Files.py'
# # data = read_txt_file(f'{path}/{filename}', True)
# data = read_txt_file(os.path.join(path, filename))
#
# for filename in list_dir:
#     filepath = os.path.join(path, filename)
#     if os.path.isfile(filepath):
#         print(filepath)

##################################################
# импорт функций

# from utils.Files import read_txt_file
# data = read_txt_file('TEST.txt', True)

# типы переменных / анатация типов
# def read_txt_file(filename: str, debug_mode: bool = True) -> str:
#     with open(filename, 'r') as my_file:
#         data = my_file.read()
#     if debug_mode:
#         print(data)
#     return data
#
#
# data = read_txt_file('TEST.txt', True)


# ***********************************************************
# параметры по умолчанию

# def get_args(*args, **kwargs):
#     for arg_value in args:
#         print(arg_value)
#     for kwarg_value in kwargs:
#         print(kwarg_value, kwargs[kwarg_value])
#
# get_args(1, 2, 'qwe', name='John', age=12)


# **************************************************************

# def read_txt_file(filename):
#     with open(filename, 'r') as my_file:
#         data = my_file.read()
#     return data
#
#
# data = read_txt_file('TEST.txt')
# print(data)


# def read_txt_file(filename='TEST.txt'):
#     with open(filename, 'r') as my_file:
#         data = my_file.read()
#     return data
#
#
# data = read_txt_file()
# print(data)
# from random import randint, choice
# from string import ascii_lowercase
#
#
# names = ["king", "miller", "kean", "smith"]
# domains = ["net", "com", "ua"]
# DEBUG_MODE = True
#
#
# def create_email(mail_domains, mail_names, debug_mode=DEBUG_MODE):
#     alphabet = ascii_lowercase
#     position_before_at = choice(mail_names) + '.' + str(randint(100, 999))
#     position_after_at = [choice(alphabet) for _ in range(0, randint(5, 7))]
#     domain = choice(mail_domains)
#     e_mail_name = position_before_at + '@' + ''.join(position_after_at) + '.' + domain
#     if debug_mode:
#         print(e_mail_name)
#     return e_mail_name
#
#
# e_mail = create_email(domains, names)
#
#
# def read_txt_file(filename='TEST.txt', debug_mode= False):
#     with open(filename, 'r') as my_file:
#         data = my_file.read()
#     if debug_mode:
#         print(data)
#     return data
#
#
# data = read_txt_file(debug_mode=DEBUG_MODE)
