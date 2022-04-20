def read_txt_file(filename):
    with open(filename, 'r') as my_file:
        data = my_file.read()
    return data


def write_txt_file(filename, data):
    with open(filename, 'w') as txt_file:
        txt_file.write(data)


filename = "lesson_test.txt"
data = read_txt_file(filename)

numbers = []
for line in data.split("\n"):
    if line:
        number = line.split()[1]
        numbers.append(number)
print(numbers)

# '\t'

data += "TEST"

output_filename = "lesson_test_2.txt"
write_txt_file(output_filename, data)

#####################################################################################
# my_list = [1, -2, 3, 4, -5]
#
# # result = [number for number in my_list if number > 0]
# # result = [number ** 2 if number < 0 else number for number in my_list]
# result = [number ** 2 if number < 0 else number for number in my_list if not number % 2]
#
# print(result)
#####################################################################################
# import random
# import string
#
# random_len = random.randint(5, 7)
# rand_symbol_list = [random.choice(string.ascii_lowercase) for _ in range(random_len)]
# print(rand_symbol_list)