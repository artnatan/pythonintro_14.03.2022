#работа с файлами
# модуль os

filename = 'lesson_4.py'
# # my_file = open(filename, 'r')
# data = my_file.read()
# # my_file.close()
# #
# # print(data)
#
with open(filename, 'r') as my_file:
    data = my_file.read()
#     # first_line = my_file.readline()
#     # second_line = my_file.readline()
#     # data = my_file.readline()
#
# # print(first_line, second_line)
# # print(data)
# print(data)

# data.append("test text \n")
data = data.split('\n')
data.append("test text \n")
"\n".join(data)
with open(filename.replace('.py', '_test.txt'), 'w') as txt_file:
    txt_file.writelines(data)
