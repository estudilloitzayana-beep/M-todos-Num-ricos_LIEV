def k(x):
     return((x**2)-1)/3

def f(x):
    return(2/3)*x

p0=1/2

for i in range(10):
    pm=(p0)-(k(p0)/f(p0))
    p0=pm
    print(pm)