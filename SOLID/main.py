class App:
    def __init__(self):
        cat = Cat()
        cat.walk()

class Animal:
    def walk(self):
        print("Animal walk!")

class Cat(Animal):
    def __init__(self):
        super().__init__() 
        print("Yeay! Cat walk!")

app = App()
