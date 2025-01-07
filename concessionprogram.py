menu = {"pizza" : 3.00,
        "popcorn" : 5.00,
        "nachos" : 4.50,
        "french fries" : 10.00,
        "soda" : 3.00
        }
cart = []
total = 0

print("-" * 10 + "MENU" + "-" * 10)
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("-" * 24)

while True:
    food = input("Select an item from the menu (q to quit)")
    if food == "q":
        break
