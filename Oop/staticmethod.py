# Static methods = A method that belong to a class rather than any object from that class (instance)
#                   Usually used for general utillity functions

# Instance Methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data




class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position

#INSTANCE METHOD
    def get_info(self):
        return f"{self.name} = {self.position}"
    
#STATIC METHOD
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cooker","Janitor"]
        return position in valid_positions


employee1 = Employee(name="Pedro",position="Manager")
employee2 = Employee(name="Ph",position="Cashier")
employee3 = Employee(name="Ruan",position="Cooker")


print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())