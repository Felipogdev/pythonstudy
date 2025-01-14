# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#               Benefit: Add aditional logic when read, write or delete attributes
#               Gives you getter, setter and deleter method

class Rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height = height


    #Getters
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    #Setters
    @width.setter
    def width(self,new_width):
        if new_width >0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self,new_height):
        if new_height >0:
            self._width = new_height
        else:
            print("Height must be greater than 0")
    #Deleter
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectangle(width=10,height=5)
#using the setter, it changes the private attribute
rectangle.width = 4


#Acessing the getter
print(rectangle.width)
print(rectangle.height)

#Deleting attributes
del rectangle.width
del rectangle.height

