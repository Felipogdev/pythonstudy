#collection = single 'variable' used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Turple = () ordered and unchangeable. Duplicates OK. FASTER
#Dictionary = {} a collection of {key : value} pairs ordered and changeable. No duplicates

dictionary = { "Brasil" : "Brasilia", "Portugal" : "Lisboa", "Argentina" : "Buenos Airies"}

#.items() retorna um tuple
#print(dictionary.items()) retornaria [("Brasil", "Brasilia"), ("Portugal", "Lisboa"), ("Argentina", "Buenos Airies")]

#Cada iteração do loop, ele pega o key do primeiro tuple e o value do primeiro tuple e repete, e vai loopando
for key, value in dictionary.items():
    print(key)
    print(value)

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("Japan"))

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist")
#.update() muda o value de uma key
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
#capitals.pop("China")

#.popitem() remove a ultima key do dic
capitals.popitem()
capitals.clear()

keys = capitals.keys()
for key in capitals.keys():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")

