import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7],
              [8, 9, 10, 11, 12, 13, 14]])
print(a)

#Get a specific element [r, c]
print(a[1, 3])

#Get a specific row
print(a[0, :])

#Get a specific column
print(a[:,2])
print("Teste")
print(a[0,1:6:2])
print(a[1,0:7:3])
