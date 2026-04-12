def f(x):
    return (x**2-1)/3   

a = 0
b = 2

print("="*32)
print(f"{'Iteración':^10} | {'Aprox raíz':^14}    |")
print("="*32)

for i in range(10):
    xr = b - (f(b) * (a - b)) / (f(a) - f(b))
    print(f"{i:^10} | {xr:^14.15f} |")
    
    if f(a) * f(xr) < 0:
        b = xr
    else:
        a = xr