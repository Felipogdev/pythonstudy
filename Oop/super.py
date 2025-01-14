#super() = Function used in a child class to call methods from a parent class (superclass)
#           Allows you to extend the functionality of the inherited methods


class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

#super() is used to reuse a constructor of a parent class
class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a cirle with an area of {3.1415 * self.radius * self.radius:.2f}cm²")
        super().describe()

class Square(Shape):
    def __init__(self,color, is_filled, width):
        super().__init__(color,is_filled)
        self.width = width
    def describe(self):
        print(f"It is a square with an area of {self.width * self.width:.2f}cm²")
        super().describe()

class Triangle(Shape):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {(self.width * self.height)/2:.2f}cm²")
        super().describe()


circle = Circle(color="Red",is_filled=True,radius=10)
circle.describe()

square = Square(color="Blue",is_filled=False,width=10)
square.describe()

triangle = Triangle(color="Yellow",is_filled=False,width=10,height=5)
triangle.describe()
