import matplotlib.pyplot as plt
import numpy as np 

Cantidad = np.array([3.600, 25.000, 8.000, 8.200,5.500])
Electrodomesticos = ["Televisores", "Celulares", "Pava Electrica", "Monitores", "Equipos de Musica"]

plt.pie(Cantidad, labels=Electrodomesticos)
plt.title("Electrodomesticos")
plt.show()

