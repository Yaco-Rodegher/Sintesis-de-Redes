# Codigo de pyton para graficar la funcion de transferencia de un filtro rechaza banda 
# Conlas variables Wz (frecuencia del cero) , Wp (frecuencia del polo) y el factor de calidad Qp 

import control as ctrl
import matplotlib.pyplot as plt

# Parámetros ajustables del filtro
w_z = 1000 # Frecuencia de los ceros (rad/s)
w_p = 1000  # Frecuencia de los polos (rad/s)
Q_p = 0.4     # Factor de calidad de los polos (ajusta el ancho de banda rechazado)

# Función de transferencia: (s^2 + w_z^2) / (s^2 + (w_p/Q_p)*s + w_p^2)
s = ctrl.tf('s')
H = (s**2 + w_z**2) / (s**2 + (w_p/Q_p)*s + w_p**2)

# Graficar Mapa de Polos y Ceros y Diagrama de Bode
plt.figure(1); ctrl.pzmap(H)
plt.figure(2); ctrl.bode(H, dB=True)
plt.show()

# En el pdf se ve los graficos para diferentes Qp, visualizando como cambia la respuesa al desplazarse los polos. 
