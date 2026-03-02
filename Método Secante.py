import math

def Secante(x):
    return (x**2-1)/3

p0=int(input("Ingresa el primer valor para p0: "))
p1=int(input("Ingresa el valor el segundo valor para p1: "))
iteraciones=int(input("Ingrese cuantas iteraciones desa realizar: "))

while Secante(p0)-Secante(p1)==0:
    print("El valor ingresado es incorrecto.")
    p0=int(input("Ingresa el primer valor para p0: "))
    p1=int(input("Ingresa el valor el segundo valor para p1: "))
    

for i in range (iteraciones):
    if Secante(p0)-Secante(p1)==0:
        print("Incorrecto")
        break
    pm=p0-(p0-p1)*Secante(p0)/(Secante(p0)-Secante(p1))
    print (pm)
    p0=p1
    p1=pm
    