########################домашка##############################

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

