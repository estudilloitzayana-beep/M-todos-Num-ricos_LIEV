import math

def f(x):
    return x - 0.8 - 0.2*math.sin(x)

a = 0
b = 1

print("="*53)
print(f"{'Iteración':^10} | {'Aprox raíz':^14}    | {'Evaluación raíz':^14}    |")
print("="*53)

for i in range(10):
    p = b - (f(b) * (a - b)) / (f(a) - f(b))
    print(f"{i:^10} | {p:^14.15f} | {f(p):^14.15f} |")
    
    if f(a) * f(p) < 0:
        b = p
    else:
        a = p