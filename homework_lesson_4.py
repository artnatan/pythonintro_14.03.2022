# 1) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно половине значения value, в противном случае - противоположне value число

value = 60
new_value = value / 2 if value < 100 else -value
print(new_value)

# 2) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно 1, в противном случае - 0

value = 101
new_value = 1 if value < 100 else 0
print(new_value)

# 3) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно True, в противном случае - False

value = 99
new_value = True if value < 100 else False
print(new_value)

# 4) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки себя же.
# Пример: # было - "qwer", стало - "qwerqwer". Если длинна не меньше 5, то оставить строку как есть.

my_str = 'qwer'
if len(my_str) < 5:
    my_str += my_str
    print(my_str)
else:
    print(my_str)

# 5) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки перевернутую себя же.
# Пример: было - "qwer", стало - "qwerrewq". Если длинна не меньше 5, то оставить строку как есть.

my_str = 'qwer'
if len(my_str) < 5:
    my_str = my_str + my_str[::-1]
    print(my_str)
else:
    print(my_str)

# 6) Доработать задание с калькулятором, чтобы в конце вычисления у пользователя спрашивало, нужен ли калькулятор еще.
# И если да, то запустить вычисление заново



########################Калькулятор##############################

# код калькулятора ниже и по ссылке
# https://github.com/artnatan/pythonintro_14.03.2022/blob/main/homework_calc.py

restart = 'y'

while restart == 'y':

    #выбор операции
    input_case = input('Выбери тип операции: \n1 +\n2 -\n3 *\n4 /\n')

    #проверка ввода операции. Обнаружил, что при нажатии Enter, в переменную записывает значение пустой строки,
    #которая (почему то) проходит проверку input_case in '1234'. Поэтому добавил проверку на "".
    if input_case != '' and input_case in '1234':
        # задаем значения переменных
        value_1 = input("введи число: ")
        value_2 = input("введи число: ")

        # проверка введенных значений
        try:
            value_float_1 = float(value_1)
            value_float_2 = float(value_2)

            # решение задачи
            if input_case == '1':
                result = value_float_1 + value_float_2
                print(f'Ответ: {result}')
            elif input_case == '2':
                result = value_float_1 - value_float_2
                print(f'Ответ: {result}')
            elif input_case == '3':
                result = value_float_1 * value_float_2
                print(f'Ответ: {result}')
            elif input_case == '4':
                result = value_float_1 / value_float_2
                print(f'Ответ: {result}')

        except ValueError:
            print('Введено не число')
        except ZeroDivisionError:
            print('На ноль делить нельзя')

    else:
        print('Введен не существующий тип операции')

    #делаем выбор перезапуска программы
    #также делаем проверку на ввод верных значений. Если значения не из списка, повторяем вопрос
    check = True
    while check:
        restart = input('\nПродолжить вычисления - "y"; прекратить - "n": ')
        check = False if restart != '' and restart in 'yn' else True