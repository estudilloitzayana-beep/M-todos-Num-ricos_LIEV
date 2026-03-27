import math

def f(x):
    return math.exp(-x)-x

p0=0
p1=1

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
        
if pm == p0 or pm==p1:
    print("La sucesión oscila entre dos valores")
else:
    print("La sucesión converge")
    
