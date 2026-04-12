def f(x):
    return x**3 - 3*x + 1   

a = 0
b = 1

print("="*93)
print(f"{'n':^10} | {'a':^14}    | {'b':^14}    | {'p':^14}    | {'f(p)':^14}     |")
print("="*93)

for i in range(10):
    p = b - (f(b) * (a - b)) / (f(a) - f(b))
    print(f"{i:^10} | {a:^14.15f} | {b:^14.15f} | {p:^14.15f} | {f(p):^14.15f} |")
    
    if f(a) * f(p) < 0:
        b = p
    else:
        a = p