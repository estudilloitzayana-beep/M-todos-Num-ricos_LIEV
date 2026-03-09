def f(x):
    return x**2-2

def g(x):
    return 2/x

p0=1

for i in range(10):
    q=g(p0)
    p0=q
    print(q)
    
if q == p0:
    print("La sucesión oscila entre dos valores")
else:
    print("La sucesión converge")