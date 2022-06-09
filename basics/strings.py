"==================Строки===================="
# строки - тип данных, который предназначен для хранения текста (последовательности символов), заключенного в одинарные или двойные кавычки
# Синтаксис:
string1 = 'строка с одинарными кавычками'
string2 = "строка с двойными кавычками"
# error = 'неправильная строка"

"============Экранизация строк==============="
# экранизация спец-символов
'\n' #перенос на новую строку
'\t' #табуляция
'\v' #вертикальная табуляция
'\\' # отображение \ (потому что он является инструкцией, которая влияет на наш код)'
'\'' # отображение '
"\"" # отображение "
'\r' # возвращение каретки в начало строки и перезаписывает продолжающими данными

"=============Форматирование строк============="

# format2 = 'Название: %s, Цена: %s
# print (format2 % ("Гуляш", "250"))
# print (format2 % ("Самсы", "70")), sep = (' ')

#format3 = 'Название: {}, Цена: {}'
# print(format3.format('Шакарап', '35'))

# f' {}  {}'

"=================Методы строк================="
# методы типов данных - функции, к которым мы обращаемся через точку
dir(str) # функция dir позволяет посмотреть все методы класса (типа данных)

'HELLO'.lower() # 'hello'
'hello'.upper() # 'HELLO'
'Hello'.swapcase # 'hELLO'
'hello'.title() # 'Hello'
'hello world'.title() # 'Hello World'
'hello world'.capitalize() # 'Hello world'

'hello'.center(11) # '   hello   '
'hello'.center(11, '-') # '---hello---'

'hello'.count('l') # 2
'hello'.count('ll') # 1
'hello hello'.count('hello') # 2
'hello'.count('w') # 0

'hello world'.startswith('hell') # True
'hello world'.endswith('d') # True
'hello world'.startswith('H') # False

'hello world'.find(' ') # 5
'hello world'.find("o") # 4
'hello world'.find('wo') # 6

'hello world'.split() # ('hello world')
'hello world'.split('o') # ('hell', ' w', 'rld')

'$'.join(['hello', 'world']) # hello$world
' '.join(list('hello')) # 'h e l l o'


"==================Индексы==================="
# индекс - порядковый номер символа в строке
'h e l l o   w o r l d'
#0 1 2 3 4 5 6 7 8 9 19
string = 'hello world'
string[0] # h
string[10] # d
string[5] # ' '

# срез - подстрока строки
string[0:5] # 'hello'
string[0:5][2:4] # 'll'

# конкатенация - склеивание строк



