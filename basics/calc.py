contin = 'y'
while contin == 'y':
    first_num = float(input('\nВведите первое число: '))
    operation = input('Выберите операцию из следующих (+, -, /, *, %, **, //): ')
    second_num = float(input('Введите второе число: '))
    if operation == '+':
        print('\nРезультат: ',first_num + second_num)
    elif operation == '-':
        print('\nРезультат: ', first_num - second_num)
    elif operation == '/':
        print('\nРезультат: ', first_num / second_num)
    elif operation == '*':
        print('\nРезультат: ', first_num * second_num)
    elif operation == '%':
        print('\nРезультат: ', first_num % second_num)
    elif operation == '**':
        print('\nРезультат: ', first_num ** second_num)
    elif operation == '//':
        print('\nРезультат: ', first_num // second_num)
    else:
        print('\nДанной операции нет в системе\n')
    contin = input('\nВведите "y", чтобы продолжить\nЛюбую другую клавишу, чтобы закончить: ')
