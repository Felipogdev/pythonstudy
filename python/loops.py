#While Loop
name = input("Digite seu nome: ")

while name == "":
    print("Você não digitou seu nome")
    name = input("Digite seu nome: ")
print(f"Seu nome é {name}")

#For loop
# for i in range(1,11): Faz a mesma coisa
for i in range(10):
    print(f"{i+1}")
#Intera ao contrário com a função reversed
for i in reversed(range(10)):

#for i in range(1,11,2): 2 seria o step, então vai contar de 2 em 2
    print(f"{i+1}")

