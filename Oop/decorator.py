#Decorator = A function that extends the behavior of another function
#           without modyfying the base function
#           Pass the base function as an argument to the decorator

def add_sprinkles(func):
    def wrapper():
        print(f"You added sprinkles")
        func()
    return wrapper

@add_sprinkles
def get_ice_cream():
    print(f"This is your icecream ")

get_ice_cream()


#           @add_sprinkled
#           get_ice_cream("Vannilla")