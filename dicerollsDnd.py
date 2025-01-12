import random
numDices = int(input("Digite o numero de dados que deseja rolar: "))
facesDices = int(input("Digite o numero de faces que deseja rolar: "))

for i in range(numDices):
    numRolled = random.randint(0,facesDices)
    print(numRolled)