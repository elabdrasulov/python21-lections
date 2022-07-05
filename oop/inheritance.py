"Наследование - принцип ООП, где мы можем в дочернем классе унаследовать переопределять и использовать все атрибуты и методы родительского класса"

class A:
    def method(self):
        print("method in class A")

obj_a = A()
obj_a.method() # method in class A

class B(A):
    """
    Наследовали все методы и атрибуты класса А
    """
obj_b = B()
obj_b.method # method in class A

"class A - родительский класс"
"class B - дочерний класс"

class C(A):
    """
    Наследовали все методы и атрибуты у класса А,\n
    а также переопределили метод method
    """
    def method(self):
        print("method in class C")


obj_a = A()
obj_a.method() # method in class A

obj_c = C()
obj_c.method() # method in class C

"Переопределение - даем то же название, но другое знчение"

"super() - функция, которая позволяет обратиться к родительскому классу и вызвать определенные методы или атрибуты"

class A:
    def my_range(self, n):
        return list(range(0, n+1))

class B(A):
    def my_range(self):
        # через super мы обращаемся к методу родительского класса
        return super().my_range(10)

obj_a = A()
obj_a.my_range(3) # [0,1,2,3]

obj_b = B()
obj_b.my_range() # [0,1,2,3,4,5,6,7,8,9,10]


"================ Виды наследований ==============="

# одиночное наследование
# множественное наследование
# многоуровневое наследование
# иерархическое наследование
# гибридное наследование