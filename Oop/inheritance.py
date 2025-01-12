#Inheritance = Allows a class to inhert attributes and methods
#               class Child(Parent)

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def bark(self):
        print(f"AUAU!")
    pass


class Cat(Animal):
    def meow(self):
        print("Meow")
    pass

class Mouse(Animal):
    pass

dog = Dog(name="Thor")
cat = Cat(name="Garfield")
mouse = Mouse(name="Mickey")

print(f"{dog.name} {cat.name} {mouse.name}")

dog.sleep()
cat.eat()
mouse.sleep()
dog.bark()
cat.meow()