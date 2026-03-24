import math

def x1(x2,x3):
    return (1/6)+((math.cos(x2*x3))/2)

def x2(x1,x3):
    return (1/9)*math.sqrt(x1**2+math.sin(x3)+1.06)-0.1

def x3(x1,x2):
    return ((-math.exp(-x1*x2))/20)-((10*math.pi-3)/60)

p1=0.2
p2=0.1
p3=-0.1

for i in range(1):
    q1=x1(p2,p3)
    print(q1)

    q2=x2(p1,p3)
    print(q2)

    q3=x3(p1,p2)
    print(q3)

