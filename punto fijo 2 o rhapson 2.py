import math

def funciones(x):
    f=-x**2+x+0.75
    return f

def m(y, x):
    g=math.sqrt(y+5*x*y)
    return g

p0=0

print("="*52)
print(f"{'Iteraciones':^10}| {'Funcion x':^14}    | {'Función y':^14}    |")
print("="*52)

for i in range(30):
    q=funciones(p0)
    p=m(p0, p0)
    p0=q
      
    print(f"{i:^10} | {p:^14.15f} | {q:^14.15f} |")
print("="*52)
