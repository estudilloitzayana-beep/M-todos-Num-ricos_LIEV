#Grafica del coseno hiperbolico
import numpy as np
import matplotlib.pyplot as plt 

x=np.linspace(-5, 5, 100)
y=np.cosh(x)

plt.plot(x, y)
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Grafica del coseno hiperbolico")
plt.grid()

plt.savefig("Coseno_hiperbolico.pdf")

plt.show()