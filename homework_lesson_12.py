# Написать класс и реализовать его методы: (основа - ДЗ № 11)
#
# 1. Инициализация класса с одним параметром - имя директории.
#
# 2. Написать метод экземпляра класса, который создает атрибут экземпляра класса в ввиде словаря
# {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
# Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))
#
# 2. Написать метод экземпляра класса, которая получает булевое значение (True/False).
# Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
# Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.
#
# 3. Написать метод экземпляра класса, которая получает строку, которая может быть
# или именем файла, или именем папки. (В имени файла должна быть точка).
# В зависимости от того, что функция получила (имя файла или имя папки) - записать его в соответствующий список
# и вернуть обновленный словарь.
#
# 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
# Написать метод экземпляра класса, которая получает имя директории.
# Функция проверяет соответствие полученного словаря и реальной файловой системы в полученной папке и,
# если надо, создает нужные папки и пустые файлы, в соответствии со структурой словаря.
import os


class WorkWithFolders:
    def __init__(self, dirname_exist: str, dirname_new: str, file_dir_name: str, sort_rev: bool = True):
        self.dirname_exist = dirname_exist
        self.sort_rev = sort_rev
        self.file_dir_name = file_dir_name
        self.dict_dirs_files = self.create_dict_lists()
        self.dirname_new = dirname_new

    def create_dict_lists(self):
        list_dirs_files = os.listdir(self.dirname_exist)
        dict_dirs_files = {'filenames': [],
                           'dirnames': [],
                           }

        for obj in list_dirs_files:
            dir_path = os.path.join(self.dirname_exist, obj)
            if os.path.isfile(dir_path):
                dict_dirs_files['filenames'].append(obj)
            elif os.path.isdir(dir_path):
                dict_dirs_files['dirnames'].append(obj)
        return dict_dirs_files

    def sort_dict_lists(self):
        self.dict_dirs_files['filenames'].sort(reverse=not self.sort_rev)
        self.dict_dirs_files['dirnames'].sort(reverse=not self.sort_rev)

    def add_files_dirs_to_dict(self):
        if '.' in self.file_dir_name:
            self.dict_dirs_files['filenames'].append(self.file_dir_name)
        else:
            self.dict_dirs_files['dirnames'].append(self.file_dir_name)

    def create_new_files_dirs(self):
        os.makedirs(self.dirname_new, exist_ok=True)
        for key, list_obj in self.dict_dirs_files.items():
            for obj in list_obj:
                dir_path = os.path.join(self.dirname_new, obj)
                if not os.path.exists(dir_path) and key == 'filenames':
                    with open(dir_path, 'w') as file:
                        file.write('')
                elif key == 'dirnames':
                    os.makedirs(dir_path, exist_ok=True)


dirname_exist = 'alphabet'  #имя директории для создания словаря
sort_direct = False     #параметр направления сортировки
file_dir_name = 'dir.txt'   #имя папки/файла для добавления в словарь
dirname_new = 'D_homework'  #имя директории для создания объектов из словаря

worker = WorkWithFolders(dirname_exist, dirname_new, file_dir_name, sort_direct)

print(worker.dict_dirs_files)
worker.sort_dict_lists()
worker.add_files_dirs_to_dict()
print(worker.dict_dirs_files)
worker.create_new_files_dirs()

