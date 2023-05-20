import numpy as np
import matplotlib.pyplot as plt

eixoX = np.array([0, 1, 2, 3, 5])
eixoY = np.array([3, 8, 1, 10, 7])

plt.plot(eixoX, eixoY, 'o--r', ms =20, mfc='g', mec = 'b')

plt.show()
