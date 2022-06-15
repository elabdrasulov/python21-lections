"==============List================"
# списки - изменяемый, индексиремый, упорядоченный, итерируемый тип данных, предназначенный для хранения любых данных в определенном порядке

list_ = [1, 2, 4, 'hello', [0.1, 2], {"a":3}]
list_[1] # 2
list_[4] # [0.1, 2]
list_[4][0] # 0.1
list_[3][0] # 'h'
list_[-1]["a"] # 3


"=========Создание списков==========="
list1 = [1,2,3]
list2 = list('hello') # ['h','e','l','l','o']


"==========Методы списков==========="
# append добавляет элемент в конец списка
list_ = []
list_.append(1)
print(list_) # [1]
list_.append("hello")
print(list_) # [1, "hello"]
list_.append([1,2,3,4]) 
print(list_) # [1, "hello", [1,2,3,4]]
list_.append(1,2,3) # TypeError: append() takes exactly one argument (3 given)

# clear очищает список
list_.clear()
print(list_) # []

# count считает количество принятого элемента в списке
list_ = [1,2,1,4,1,5,1,7,2,4,4]
list_.count(1) # 4
list_.count(2) # 2
list_.count(4) # 3

list_ = ['hello', 'hello', 'hello']
list_.count('h') # 0
list_.count('hello') # 3
len(list_) # 3

# len считает количество обьектов в списке
list_ = [1, 2, [3, 4, 5], 6, 7, [8, 9, 10]]
len(list_) # 6

# extend добавляет элементы второго списка в первый, изменяя первый
list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1) # [1,2,3,4,5,6]
print(list2) # [4,5,6]

# index возвращает индекс первого вхождения принятого элемента
list1 = [1,2,3,4,1,2,3,5,4,1]
list1.index(3) # 2
list1.index(1) # 0

# insert добавляет элемент по индексу list.insert(index, obj)
list_ = [1,2,3]
list_.insert(0, "hello")
print(list_) # ["hello", 1, 2, 3]
list_.insert(2, 10) 
print(list_) # ["hello", 1, 10, 2, 3]
list_.insert(100, "bye")
print(list_) # ["hello", 1, 10, 2, 3, "bye"]

# pop удаляет элемент из списка по индексу и результатом отработанного метода будет удалененый элемент
list_ = [1,2,3,4,5,6,7]
popped = list_.pop()
print(list_, popped) # [1,2,3,4,5,6]  7
popped = list_.pop(1)
print(list_, popped) # [1,3,4,5,6]  2

# remove удаляет первый принятый элемент в списке
list_ = [1,2,34,1,2,3,1,2,4,1,2,6]
list_.remove(2)
print(list_) # [1, 3, 1, 2, 3, 1, 2, 4, 1, 2, 6]
print(str(list_))

# reverse изменяет список, расставляя его элементы в обратном порядке
list_ = [1,2,3,4,5]
list_.reverse()
print(list_) # [5,4,3,2,1]
new_list = list_[::-1] # [1,2,3,4,5]

# sort сортирует список, состоящий из элементов одного типа данных в возрастающем порядке (алфавитном для строк)
list_ = [2,1,5,3,8,4,7,6,10,9]
list_.sort()
print(list_) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_ = ['a', 'c', 'd', 'b', 'f', 'e', 'A', 'C', 'B']
list_.sort()
print(list_) # ['A', 'B', 'C', 'a', 'b', 'c', 'd', 'e', 'f']

list_ = [1,2,3,'hello'] # TypeError: '<' not supported between instances of 'str' and 'int'
list_.sort()

# reverse=True сортирует по убыванию
list_ = [2,1,5,3,8,4,7,6,10,9]
list_.sort(reverse=True) # [10,9,8,7,6,5,4,3,2,1]

"=============Tuple================"
# кортеж - неизменяемый, индексиремый, упорядоченный, итерируемый тип данных, предназначенный для хранения любых данных в определенном порядке (в целом не отличается от списков, просто не изменяемый, поэтому занимает меньше памяти)

tuple1 = (1,2,3) # (1,2,3)
tuple2 = ('hello', 2.5, 19, (2,3), [1,2,3])
tuple3 = tuple('hello') # ('h', 'e', 'l', 'l', 'o')
tuple4 = tuple([1,2,3]) # (1,2,3)

tuple4 = 1,2,3 # (1,2,3)
tuple5 = (5) # 5 (int)
tuple6 = 5, # (5,)
tuple7 = 'hello',


"==========Методы tuple============"
# count считает количество принятого элемента в кортеже
list_ = (1,2,1,4,1,5,1,7,2,4,4)
list_.count(1) # 4
list_.count(2) # 2
list_.count(4) # 3

list_ = ('hello', 'hello', 'hello')
list_.count('h') # 0
list_.count('hello') # 3
len(list_) # 3

# index возвращает индекс первого вхождения принятого элемента
list1 = (1,2,3,4,1,2,3,5,4,1)
list1.index(3) # 2
list1.index(1) # 0

"=============Создание словарей================"
dict1 = {"a":3}
dict2 = dict( [ ('key1', 'value1'), ('key2', 'value2') ] )
# dict2 = {'key1':'value1', 'key2':'value2'}
dict3 = dict( ( ['key1', 'value1'], ('key2', 'value2') ) )
# dict3 = {'key1':'value1', 'key2':'value2'}
dict4 = dict(['ab', 'cd', 'de'])
# dict4 = {"a":"b", 'c':'d', 'd':'e'}
key1, value1 = 'ab'
dict4[key1] = value1
key2, value2 = 'cd'
dict4[key2] = value2
key3, value3 = 'de'
dict4[key3] = value3


dict5 = dict(['abc']) # ValueError: dictionary update sequence element #0 has length 3; 2 is required
key1, value1 = 'abc' #
dict5[key1] = value1
