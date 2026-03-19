def f(n, m):
    s = ''
    while n > 0:
        s = str(n%m)+s
        n //= m
    return s
# c = 0
# a = 2 * 2187**2020 + 729**2021 - 2* 243**2022 + 81**2023 - 2* 27**2024 - 6561
# while a > 0:
#     if a%27 > 9:
#         c += 1
#     a //= 27
# print(c)

# for x in '0123456789ABCDEFGHIJKLMNOPQRS':
#     a = int('923'+x+'874',29) + int('524'+x+'6152',29)
#     if a%28 == 0:
#         print(x, a//28)
d = []
for x in range(2031):
    k = 0
    a = 6**2030 + 6**100 - x
    while a > 0:
        if a%6==0:
            k+=1
        a//=6
    d.append(k)
print(min(d))
