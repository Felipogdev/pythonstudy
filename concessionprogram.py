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
    food = input("Selecione um item no menu (digite q para sair)")
    if food == "q":
        break
    elif food in menu:
        cart.append(food)
        total += menu[food]
        print(f"Adicionado {food} ao carrinho. Valor total atual: ${total:.2f}")
    else:
        print("Item não está no menu. Por favor, selecione uma opção válida")

print("Seu carrinho: ")
for item in cart:
    print(f"- {item}")
print(f"Total = ${total:.2f}")