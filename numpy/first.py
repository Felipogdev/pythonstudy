import numpy as np

a = np.array([1,2,3])

b = np.array([[9.2, 6.1, 3.3],
              [5.3, 3.3, 9.3]])

#Specify data type
c = np.array([1,2,3], dtype='int16')

print("Get dimension")
print(a.ndim)
print(b.ndim)

print("Get Shape")
print(a.shape)
print(b.shape) #Output (2,3) 2 rows, 3 columns

print("Get Type")
print(a.dtype)
print(b.dtype)

print("Get size")
print(a.itemsize)
print(b.itemsize)

print("Get total size")
print(a.size * a.itemsize) #Number of elements * Itemsize
print(b.nbytes) #Same thing





