import math

def f(x):
    return 1/(x-1)

p0=0.9
p1=1.1

print("="*51)
print(f"{'iteraciones':^10} | {'pm':^14}     | {'f(pm)':^14} |")
print("="*51)

for i in range (10):
    if f(p0)-f(p1)==0:
        print("división entre cero")
        break
    pm=p1-(((p1-p0)*f(p1))/(f(p1)-f(p0)))
    print(f"{i:^10} | {pm:^14.15f} | {f(pm):^14.2f}  |")
    p0=p1
    p1=pm