def f(n, m):
    s = ''
    while n > 0:
        s = str(n%m)+s
        n //= m
    return s
d = []
for n in range(1,1000):
    x = f(n, 2)
    if n%3 == 0:
        x += x[-3:]
    else:
        x += f(((n%3)*3), 2)
    r = int(x,2)
    if r < 130:
        d.append(n)
        print(n)