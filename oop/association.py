"============= Ассоциация ==============="
# Ассоциация - принцип ООП, в котором для класса друг с другом связаны
# ассоциация делится на 2 принципа
# 1 - агрегация (более слабая связь)
# 2 - композиция (более сильная связь)


class Battery:
    power = 100
    
    def charge(self):
        if self.power < 100:
            self.power = 100

class Iphone:
    def __init__(self, color):
        self.color = color
        # когда мы создаем объект от другого класса 
        # прям внутри другого - композиция
        self.battery = Battery()

class Nokia:
    def __init__(self, color, battery):
        self.color = color
        self.battery = battery
        # когда мы принимаем уже созданный 
        # вне класса объект - агрегация

iphone = Iphone('gold')

del iphone
# объект батарейки удаляется вместе с объектом iphone
"композиция"

battery = Battery()
nokia = Nokia('black', battery)

# удаляется объект класса nokia
# объект батарейки сохраняется
"агрегация"

    
