def k(x):
     return x**3-2*x+2

def f(x):
    return 3*x**2-2

p0=0

for i in range(10):
    pm=(p0)-(k(p0)/f(p0))
    p0=pm
    print(pm)
    
if pm==0 or pm==1:
        print("Es oscilante entre 1 y 0.")
elif pm>1:
        print("Es divergente.")
else:
        print("Es convergente.")
