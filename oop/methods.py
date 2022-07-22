"============== Class, static, instance methods ================="
# instance метод (метод объекта) - метод, который принимает первым аргументом self(объект).
# Вызываем instance методы у объекта

class A:
    def instance_method(self):
        print("метод обхекта")

obj_a = A()
obj_a.instance_method() # вывзываем у объекта и 
                        # он автоматически попадает как аргумент и метод

A.instance_method(obj_a) # вызываем у класса. нужно передать объект


# class methods (метод класса) - метод, который принимает первым аргументом cls (класс)
# чтобы создать метод класса, нужно метод задекорировать classmethod

class A:
    @classmethod
    def class_method(cls):
        print(cls)
        print("метод объекта")

A.class_method()
A().class_method()


class Pizza:

    def __init__(self, radius, *ingredients):
        self.ingredients = ingredients
        self.r = radius

    def cook(self):
        print(f"Пицца размером {self.r} см\nИнгредиенты:\n{self.ingredients}")

    @classmethod
    def pepperoni(cls, r):
        return cls(r, "pepperoni", "pomidors")

    @classmethod
    def four_cheeses(cls, r):
        return cls(r, "mozzarella", "dor blu", "another one", "and another one")


pizza1 = Pizza(30, "cheese", "pomidors", "mushrooms")
pizza2 = Pizza.pepperoni(35)
pizza3 = Pizza.pepperoni(35)
pizza4 = Pizza.four_cheeses(25)
pizza5 = Pizza.four_cheeses(40)

pizzas = [pizza1, pizza2, pizza3, pizza4, pizza5]
for pizza in pizzas:
    pizza.cook()


# static методы = просто функции внутри класса, 
# которые не взаимодействуют ни с классом, ни с объектом

class Square:
    def __init__(self, a):
        self.a = a
        self.s = self.get_s(a)
    
    @staticmethod
    def get_s(a):
        return a ** 2

obj = Square(4)
print(obj.s)