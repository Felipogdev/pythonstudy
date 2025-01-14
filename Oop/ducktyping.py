#Duck Typing = Another way to achieve polymorphism besides Inheritance
#               Object must have the minimum necessary attributes/methods
#               "If it looks like a duck and quack like a duck, it must be a duck.


class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print(f"WOOF!")

class Cat(Animal):
    def speak(self):
        print(f"MEOW!")

class Car:
    alive = False
    #Se o method da função for speak, funciona
    def speak(self):
        print("HONK")


animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)