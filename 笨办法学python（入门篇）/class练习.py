class Animal():

    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}我不知道说什么")
class Dog(Animal):

    def bark(self):
        print('wangwang')
    
    def speak(self):
        parent_speak = super().speak()
        print(f"{parent_speak}{self.name} can bark like wangwang!")

a = Dog('xiaoli')
a.bark()
a.speak()