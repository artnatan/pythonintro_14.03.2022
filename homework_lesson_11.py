import os

# Все пункты являются частью одного задания, поэтому можно использовать функции несколько раз и не дублировать код.
# Если хотите, можете использовать значения по умолчанию и аннотацию типов.
#
# 1. Написать функцию, которая получает один параметр - имя директории и возвращает словарь вида
# {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
# Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))


def create_dict_lists(dirname: str) -> dict:
    list_dirs_files = os.listdir(dirname)
    dict_dirs_files = {'filenames': [],
                       'dirnames': [],
                       }

    for obj in list_dirs_files:
        if os.path.isfile(f'{dirname}\\{obj}'):
            dict_dirs_files['filenames'].append(obj)
        elif os.path.isdir(f'{dirname}\\{obj}'):
            dict_dirs_files['dirnames'].append(obj)

    return dict_dirs_files


dirname = 'alphabet'
dict_result = create_dict_lists(dirname)
print(f'1: {dict_result}')

# 2. Написать функцию, которая получает два параметра - словарь, описанный в пункте 1
# и булевое значение (True/False) - можно сделать параметром по умолчанию.
# Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
# Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.


def sort_dict_lists(dict_files_dirs: dict, sort_rev: bool =False) -> dict:
    dict_files_dirs['filenames'].sort(reverse=sort_rev)
    dict_files_dirs['dirnames'].sort(reverse=sort_rev)
    return dict_files_dirs


sort_revers = True
dict_sort = sort_dict_lists(dict_result, sort_revers)
print(f'2: {dict_sort}')

# 3. Написать функцию, которая получает два параметра - словарь, описанный в пункте 1 и строку, которая может быть
# или именем файла, или именем папки. (В имени файла должна быть точка).
# В зависимости от того, что функция получила (имя файла или имя папки) - записать его в соответствующий список
# и вернуть обновленный словарь.


def add_files_dirs_to_dict(dict_files_dirs: dict, string_name: str) -> dict:
    if '.' in string_name:
        dict_files_dirs['filenames'].append(string_name)
    else:
        dict_files_dirs['dirnames'].append(string_name)
    return dict_files_dirs


file_dir_name = 'dir'
dict_add_file_dir = add_files_dirs_to_dict(dict_result, file_dir_name)
print(f'3: {dict_add_file_dir}')

# 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
# Написать функцию, которая получает два параметра - словарь, описанный в пункте 1 и имя директории.
# Функция проверяет соответствие полученного словаря и реальной файловой системы в полученной папке и,
# если надо, создает нужные папки и пустые файлы, в соответствии со структурой словаря.


def create_new_files_dirs(dict_files_dirs: dict, dirname: str) -> None:
    os.makedirs(dirname, exist_ok=True)
    for key, list_obj in dict_files_dirs.items():
        for obj in list_obj:
            dir_path = os.path.join(dirname, obj)
            if not os.path.exists(dir_path) and key == 'filenames':
                with open(dir_path, 'w') as file:
                    file.write('')
            elif key == 'dirnames':
                os.makedirs(dir_path, exist_ok=True)


dirname = 'Directory_homework'
create_new_files_dirs(dict_result, dirname)
