def puntofijo(x):
    f=((x**2)-1)/3
    return f
p0=0

for i in range(20):
    q=puntofijo(p0)
    p0=q
    print({q})