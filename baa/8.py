from itertools import *
c = 0
for i in product('ирстуц', repeat=5):
    c +=1
    i = ''.join(i)
    if 'цц' not in i and i.count('и')==2:
        print(c, i)

def sogl(n):
    for x in 'стрвк':
        for y in 'стрвк':
            for z in 'стрвк':
                m = x+y+z
                if m not in n:
                    return True
                else:
                    return False

def glasn(n):
    for x in 'оиа':
        for y in 'оиа':
            for z in 'оиа':
                m = x+y+z
                # print(m, n)
                if m not in n:
                    return True
                else:
                    return False
c = 0
from itertools import *
for i in permutations('сортировка'):
    s= ''.join(i)
    if sogl(s) and glasn(s):
        c += 1
print(c)