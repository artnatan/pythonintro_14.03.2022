########################домашка##############################


import sys
#выбор операции
input_case = input('Выбери тип операции: \n1 +\n2 -\n3 *\n4 /\n')


#проверка ввода операции
try:

    input_case_int = int(input_case)
    if input_case_int > 4:
        print('Введен не существующий тип операции')
        sys.exit()

except ValueError:
    print('Введен не существующий тип операции')
    sys.exit()

#задаем значения переменных
value_1 = input("введи число: ")
value_2 = input("введи число: ")

#проверка введенных значений
try:
    value_float_1 = float(value_1)
    value_float_2 = float(value_2)

    # решение задачи
    if input_case_int == 1:
        result = value_float_1 + value_float_2
        print(f'Ответ: {result}')
    elif input_case_int == 2:
        result = value_float_1 - value_float_2
        print(f'Ответ: {result}')
    elif input_case_int == 3:
        result = value_float_1 * value_float_2
        print(f'Ответ: {result}')
    elif input_case_int == 4:
        result = value_float_1 / value_float_2
        print(f'Ответ: {result}')

except ValueError:
    print('Введено не число')
