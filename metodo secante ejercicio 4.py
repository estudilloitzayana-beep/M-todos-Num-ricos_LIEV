import math

def f(x):
    return -x**3 - math.cos(x)

p0=-1
p1=0

print("="*51)
print(f"{'iteraciones':^10} | {'Aprox Raíz':^14}     | {'Evaluación':^14} |")
print("="*51)

for i in range (10):
    if f(p0)-f(p1)==0:
        print("división entre cero")
        break
    pm=p1-(((p1-p0)*f(p1))/(f(p1)-f(p0)))
    print(f"{i:^10} | {pm:^14.15f} | {f(pm):^14.2f}  |")
    p0=p1
    p1=pm
   