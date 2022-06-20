from random import randint

num = randint(1, 10)

name = input('Как тебя зовут?\n') 
print(f'\n{name}, хочешь сыграть в игру "Угадай число"? (да / нет)')

contin = input().lower()
contin = 'да'
tries = 0
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

