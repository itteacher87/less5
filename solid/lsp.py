# Можно подставить объект потомка вместо объекта предка и не изенится поведение

class Animal:
    def __init__(self,name):
        self.name = name

    def voice(self):
        print('Издать звук...')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def voice(self):
        print("Мяу")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def voice(self):
        print("Гав")

cat = Cat("Барсик")
dog = Dog("Шарик")
animal = Animal('абсрактное животное')




amimals = [cat,dog]
for item in amimals:
    item.voice()