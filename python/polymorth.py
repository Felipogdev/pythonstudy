#Polymorphism = 1.Inheritance = An object could be treated of the same type as a parent class
#               2. "Duck Typing" = Object must have attributes/methods

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.1415 * self.radius * self.radius

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self,height,base):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height)/2

class Pizza(Circle):
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.topping = topping
        self.radius = radius



shapes = [Circle(radius=4), Square(side=10), Triangle(height=4,base=5),Pizza(topping="Queijo",radius=5)]

for shape in shapes:
    print(f"{shape.area():.2f}cm²")
