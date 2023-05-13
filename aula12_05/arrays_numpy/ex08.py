import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print("Dimensão: ", arr.ndim)
print("Quantidade de linhas e colunas: ", arr.shape)

novoArray = arr.reshape(-1)  # transforma em um array 1-dimensional
print(novoArray)
