import numpy as np

print("All 0s Matrix")
print(np.zeros((2,3)))

print("All 1s Matrix")
print(np.ones((2,3)))

print("Any other number")
print(np.full((2,3), 99)) #Array 2 by 3 full of 99

print("Random Decimal Numbers")
print(np.random.rand(4,2))

print("Random Ints")
print(np.random.randint(0, 100, size=(3,3)))

print("Identity Matrix")
print(np.identity(3))

print("Repeat")
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)
print(r1)

print("Desafio")
output = np.ones((5,5))
array_zeros = np.zeros((3,3))
array_zeros[1,1] = 9
output[1:-1,1:4] = array_zeros
print(output)

