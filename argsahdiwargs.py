# *args = allows you to pass multiple non-key arguments
#*adds pass the parameters to a tuple

def add (*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(4,5,10))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

# **kwargs = allows you to pass multiple keyword-arguments
# *unpacking operator
# pass the parameters to a dict

def print_addres(**kwargs):
    print("\n")
    for key,value in kwargs.items():
        print(f"{key}, {value}")

print_addres(street="Avenida Alcaides de faria",
             city="Barcelos",
             state="Braga",
             zip="4750106")