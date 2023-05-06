import numpy as np

print(np.__version__)

a = np.array([1, 2, 3, 4, 5])
print(a, "\n")

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], str)
print(b)

array = np.empty( (2, 4), float )
print(array)

a = np.eye(3,3,1)
print(a)

m = np.ones( (2,3) , float)
print(m)

n = np.zeros( (2,3), float )
print(n)

aa = np.arange(2,10,2)
print(aa)