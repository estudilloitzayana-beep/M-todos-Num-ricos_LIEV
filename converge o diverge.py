import math

def f(x):
    return math.cos(x)-x

def g(x):
    return 1/2*(x+math.cos(x))

p0=2

for i in range(15):
    q=g(p0)
    p0=q
    print(q)
    
if q == p0:
    print("La sucesión es convergente")
else:
    print("La sucesión es divergente")