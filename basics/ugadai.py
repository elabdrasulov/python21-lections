from random import randint

num = randint(1, 10)

contin = 'да'
name = input('Как тебя зовут?\n') 
tries = 0
contin = input(f'\n{name}, хочешь сыграть в игру "Угадай число"? (да / нет)\n').lower()

while contin not in ('да', 'нет'):
    contin = input('\nДа или нет?!\n').lower()
if contin == 'да':
    while contin == 'да':
        user_num = int(input('\nТвоя догадка: '))
        tries += 1
        if user_num < num:
            print('\nЭто число больше!')
        elif user_num > num:
            print('\nЭто число меньше!')
        else:
            print('\nТы угадал!')
            print(f'Количество попыток: {tries}')
            contin = input(f'\n{name}, хочешь сыграть в игру "Угадай число"? (да / нет)\n').lower()
            tries = 0

