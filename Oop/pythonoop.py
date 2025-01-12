
class Pokemon:
    # Constructor (attributes)
    def __init__(self, name, type, evo):
        self.name = name
        self.type = type
        self.evo = evo

    # Method
    def eat(self):
        print(f"{self.name} ate")

Piplup = Pokemon(name="Piplup", type="Water", evo=True)
print(f"Seu pokemon é um {Piplup.name} do tipo {Piplup.type}")
if Piplup.evo is True:
    print("Ele evolui")
else:
    print("Ele nao evolui")

Piplup.eat()

class Student:
    #num_students is a class variable
    num_students = 0
    def __init__(self,name, age):
        #Instances variables
        self.school_name = "Lusofona"
        self.name = name
        self.age = age
        #increment the class variable
        Student.num_students += 1

student1 = Student(name="Tiago",age="19")
student2 = Student(age="19",name="Pedro")
print(student2.school_name)
print(Student.num_students)