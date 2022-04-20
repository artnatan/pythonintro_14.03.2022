# Все пункты сделать как отдельные функции и их вызовы.
#
# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).

file_name = 'domains.txt'


def create_list_str(filename):
    with open(filename, 'r') as my_file:
        data = my_file.read()
    domains = []
    for domain in data.split("\n"):
        if domain:
            domains.append(domain[1:])
    return domains


list_domains = create_list_str(file_name)
print(f'1: {list_domains}')

# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"

file_name = 'names.txt'


def create_list_names(filename):
    with open(filename, 'r') as my_file:
        data = my_file.read()
    names_list = []
    for line in data.split("\n"):
        if line:
            names_list.append(line.split("\t")[1])
    return names_list


list_names = create_list_names(file_name)
print(f'2: {list_names}')

# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date": date}
# в которых date - это дата из строки (если есть),
# Например [{"date": "1st January 1919", "date": "8th February 1828"},  ...]

file_name = 'authors.txt'


def create_list_date_dicts(filename):
    with open(filename, 'r') as my_file:
        data = my_file.read()
    list_date_dict = []

    for line in data.split("\n"):
        if ' - ' in line:
            line_split = line.split(' - ')
            date_dict = {'date': line_split[0]}
            list_date_dict.append(date_dict)
    return list_date_dict


list_date = create_list_date_dicts(file_name)
print(f'3: {list_date}')

# По просьбам некоторых студентов начну включать дополнительные задания.
# 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
# Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]


def create_list_dates(filename):
    dates_dict = {'January': '01',
                  'February': '02',
                  'March': '03',
                  'April': '04',
                  'May': '05',
                  'June': '06',
                  'July': '07',
                  'August': '08',
                  'September': '09',
                  'October': '10',
                  'November': '11',
                  'December': '12',
                  }
    with open(filename, 'r') as my_file:
        data = my_file.read()
    list_date_dict = []

    for line in data.split("\n"):
        if ' - ' in line:
            line_split = line.split(' - ')
            date = line_split[0].split()
            if len(date) == 3:
                day = date[0][:-2]
                if len(day) == 1:
                    day = f'0{day}'
                date_mod = f'{day}/{dates_dict[date[1]]}/{date[2]}'
            else:
                date_mod = f'{dates_dict[date[0]]}/{date[1]}'
            date_dict = {'date_original': line_split[0],
                         'date_modified': date_mod,
                         }
            list_date_dict.append(date_dict)
    return list_date_dict


list_dates = create_list_dates(file_name)
print(f'4: {list_dates}')
