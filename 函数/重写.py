class Animal():

    def __init__(self,name):
        self._name = name

    def run(self):
        print("动物会跑")
    def sleep(self):
        print("睡觉")
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name



class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self._age = age
    def back(self):
        print("汪汪汪")
    def run(self):
        print("狗跑")

d = Dog('旺财')
d.name = '小黑'



