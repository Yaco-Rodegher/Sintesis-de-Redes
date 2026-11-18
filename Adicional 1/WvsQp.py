#Frecuencia del polo normalizada en funcion del factor de calidad Qp

import numpy as np, matplotlib.pyplot as plt

Qp = np.linspace(0.4, 2, 100)

# La deduccion de esta formula se encuentra en el archivo .png 
plt.plot(Qp, np.sqrt(((2 - 1/Qp**2) + np.sqrt((1/Qp**2 - 2)**2 + 4)) / 2))
plt.show()
