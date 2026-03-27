import math

def f(x):
    return x**3-3*x+1

p0=0
p1=0.1

print("="*51)
print(f"{'iteraciones':^10} | {'pm':^14}     | {'f(pm)':^14} |")
print("="*51)

for i in range (10):
    if f(p0)-f(p1)==0:
        print("division entre cero")
        break
    pm=p1-(((p1-p0)*f(p1))/(f(p1)-f(p0)))
    print(f"{i:^10} | {pm:^14.15f} | {f(pm):^14.2f}  |")   
    p0=p1
    p1=pm

if pm==0 or pm==0.1:
        print("Es oscilante entre 0 y 0.1")
elif pm>1:
        print("Es divergente.")
else:
        print("Es convergente.")