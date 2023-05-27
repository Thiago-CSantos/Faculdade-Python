import numpy as np
import matplotlib.pyplot as plt

y = np.array([18440, 13778, 4553, 823])
rotulos = ['Carro', 'Caminhão', 'Moto', 'Outros']
cor = ['gray','green', 'lightblue', 'orange']

plt.pie(y, labels=rotulos, startangle=90, explode=[0.03, 0.03, 0.03, 0.03], shadow=True, colors=cor, autopct="%1.2f%%")

plt.show()
