import numpy as np
import matplotlib.pyplot as plt

y = np.array([18440, 13778, 4553, 8283])
rotulos = ['Carro', 'Caminhão', 'Moto', 'Outros']
cor = ['gray', 'green', 'lightblue', 'orange']

plt.pie(y, labels=rotulos, startangle=90, explode=[0.03, 0.03, 0.03, 0.03],
        shadow=True, colors=cor, autopct="%1.2f%%")

plt.title("Ocupantes de veiculos motorizados mortos em 2003")
plt.legend(rotulos, title='Titulo da legenda', loc="center", bbox_to_anchor=(1.5, 0.5))

plt.show()
