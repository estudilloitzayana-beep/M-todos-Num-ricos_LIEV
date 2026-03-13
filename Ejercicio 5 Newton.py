def k(x):
     return x**3+x**2-1

def f(x):
    return 3*x**2+2*x

p0=0.5

print("="*51)
print(f"{'Iteración':^10} | {'Aprox Raíz':^14}     | {'f(X)':^14} |")
print("="*51)

for i in range(10):
    pm=(p0)-(k(p0)/f(p0))
    p0=pm
    print(f"{i:^10} | {pm:^14.15f} | {k(pm):^14.2e}  |")
    
print("="*51)
print(f"La raiz aproximada es: {pm}")
print("="*51)