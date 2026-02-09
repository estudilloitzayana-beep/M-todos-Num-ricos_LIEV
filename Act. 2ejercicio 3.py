import math
import matplotlib.pyplot as plt

#Parametros
x=0.5
valor_exacto=math.exp(x)

#Variables
sum=0
n_valores=[]
error_relativo=[]

#Encabezado Tabla
print("="*68)
print(f"{'n':^10} | {'Aprox e^x':^14} | {'Error Abs':^14} | {'Error Rel':^14}")
print("="*68)

#Serie Taylor
sum=0
for n in range(20):
    sum=sum+x**n/math.factorial(n)

    error_abs=abs(valor_exacto-sum)
    error_rel=error_abs/valor_exacto

    n_valores.append(n)
    error_relativo.append(error_rel)

    print(f"{n:^5.8f} | {sum:^14.8f} | {error_abs:^14.8f} | {error_rel:^14.8f}")

    if error_rel<0.10e-1:
        break
print("="*68)

print(valor_exacto)
print("="*68)
#Grafica del error relativo
plt.figure()
plt.plot(n_valores, error_relativo, marker='o')
plt.xlabel("n(grado del polinomio)")
plt.ylabel("Error relativo")
plt.title("Convergencia de la serie de Taylor e^x en 0.5")
plt.show()