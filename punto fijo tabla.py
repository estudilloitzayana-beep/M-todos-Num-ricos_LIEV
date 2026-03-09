def puntofijo(x):
    f=((x**2)-1)/3
    return f
p0=0

print("="*51)
print(f"{'Iteración':^10} | {'Aprox Raíz':^14}     | {'Evaluación Raíz':^14} |")
print("="*51)

for i in range(20):
    q=puntofijo(p0)
    p0=q
    
    
    print(f"{i:^10} | {q:^14.15f} | {puntofijo(q):^14.2e}  |")
    
    
