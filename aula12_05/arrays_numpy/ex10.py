import numpy as np

a = np.array([1, 2, 3, 4, 5, 6,5,5,5])

x = np.where(a == 5)

print(x) # retorna o indice da posição (array([4, 6, 7, 8], dtype=int64)
