import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def bisección(f, a ,b, n_iter):
    if f(a)*f(b)>0:
            raise ValueError("f(a) y f(b) deben tener signos diferentes")
    
#Punto medio inicial y lista de puntos medios.
    p_anterior=(a+b)/2
    puntos_medios=[]

#Nombres de los valores de la tabla.
    print("n     a      b      p        f(p)       error relativo")
    print("_"*65)

#ciclo principal de la bisección.
    for n in range(1, n_iter+1):
        #Calcula el punto medio del intervalo actual.
        p=(a+b)/2

        #Ver si f(p)=0
        if f(p)==0:
            print(f"{n:2d} | {a:8.6f} {b:8.6f} {p:8.6f} " 
                    f"{f(p):11.2e} {'0.00e+00':>13}")
                
            print("la raíza exacta fue encontrada")
            break  
            
        #Calcular el error relativo.
        error_rel=abs((p-p_anterior)/p)

            #Guardar los puntos medios
        puntos_medios.append(p)

            #Imprime la fila correspondiente
        print(f"{n:2d} | {a:8.6f} {b:8.6f} {p:8.6f} " 
              f"{f(p):11.2e} {error_rel:13.2e}")
                
            #En que intervalo est la raíz.
        if f(a)*f(b)>0:
            a=p
        else:
            b=p
        p_anterior=p

                #Regresa la ultima aproximación y todos los puntos medios.
    return p, puntos_medios
          
""""Ejemplo:"""

#Definimos la función.
def f(x):
    return x**3-x-2
          
#Definimos los intervalos e iteraciones.
a=1
b=2
n_iter=20

#Tolerancia.
epsilon=1e-6

#Invocamos el metodo de biseccón
raiz,puntos=bisección(f,a,b,n_iter)

#Muestra la aproximación final
print(f"Aproximación a la raiz despues de {n_iter} iteraciones: {raiz}") 

# ---------------------------------------------------------
# GRÁFICA Y ANIMACIÓN DE LA CONVERGENCIA
# ---------------------------------------------------------

# Genera puntos para dibujar la función
x = [a + i * (b - a) / 400 for i in range(401)]
y = [f(xi) for xi in x]

# Crea la figura y los ejes
fig, ax = plt.subplots()

# Dibuja la función f(x)
ax.plot(x, y, label="f(x)")

# Dibuja el eje x
ax.axhline(0, color="black")

# Configura los límites del gráfico
ax.set_xlim(a, b)
ax.set_ylim(min(y), max(y))

# Etiquetas y título
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Convergencia del método de Bisección")

# Objeto gráfico para los puntos medios (inicialmente vacío)
puntos_plot, = ax.plot([], [], 'ro', label="Puntos medios")

# Marca la raíz final
ax.plot(raiz, 0, 'ko', label="Raíz aproximada")

# Muestra la leyenda
ax.legend()

# ---------------------------------------------------------
# Función que actualiza la animación
# ---------------------------------------------------------
def actualizar(frame):
    
    x_data = puntos[:frame + 1]           # Puntos medios hasta el frame actual
    y_data = [0] * (frame + 1)             # Todos sobre el eje x
    puntos_plot.set_data(x_data, y_data)
    return puntos_plot,

# Crea la animación
anim = FuncAnimation(
    fig,
    actualizar,
    frames=len(puntos),
    interval=1000,      # Tiempo entre frames (ms)
    repeat=False
)

# Muestra la animación
plt.show()
         