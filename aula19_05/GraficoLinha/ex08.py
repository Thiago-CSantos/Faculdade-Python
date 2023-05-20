import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])

x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.ylabel("Eixo Y")
plt.xlabel("Eixo X")
plt.plot(x1, y1, '-b', label = "Linha 1")
plt.plot(x2, y2, '*--r', label = "Linha 2")

#       (eixo X), (eixo Y)
plt.axis((-2, 4, 1, 12))

plt.legend()

plt.grid(True)

plt.show()
