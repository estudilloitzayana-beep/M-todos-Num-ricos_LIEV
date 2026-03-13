import math

def k(x):
     return  math.cos(x)-2*x+3

def f(x):
    return -math.sin(x)-2

p0=1.5

print("="*51)
print(f"{'Iteración':^10} | {'Aprox Raíz':^14}     | {'f(X)':^14} |")
print("="*51)

for i in range(10):
    pm=(p0)-(k(p0)/f(p0))
    p0=pm
    print(f"{i:^10} | {pm:^14.15f} | {k(pm):^14.2e}  |")
    

    
