# a=0
# for i in range(150000, 200000):
#     c = 0
#     for j in range(2,int(i**0.5)+1):
#         if j*j==i:
#             c += j
#         elif i%j==0:
#             c += j
#             c += i//j
#     if c%13==10:
#         a+=1
#         if a<=7:
#             print(i,c)
#         else:
#             break

# n=0
# for i in range(250200, 300000):
#     c = 0
#     a=[]
#     for j in range(2,int(i**0.5)+1):
#         if j*j==i:
#             a.append(j)
#         elif i%j==0:
#             a.append(j)
#             a.append(i//j)
#     a.sort()
#     if a:
#         if (a[0]+a[-1])%123==17:
#             n+=1
#             if n<=5:
#                 print(i,a[0]+a[-1])
#             else:
#                 break

# n=0
# for i in range(550000, 600000):
#     c = 0
#     k = 0
#     for j in range(2,int(i**0.5)+1):
#         if j * j == i:
#             k+=1
#             c += j
#         elif i%j==0:
#             k += 2
#             c += j
#             c += i//j
#     if c and k:
#         f = c//k
#         if f%31==13:
#             n+=1
#             if n<=5:
#                 print(i,f)
#             else:
#                 break

# def umnoj(n):
#     u = 1
#     for i in n:
#         u *= i
#     return u
# n=0
# for i in range(400000000, 450000000):
#     p = 0
#     a = []
#     for j in range(2,int(i**0.5)+1):
#         if j * j == i:
#             a.append(j)
#         elif i%j==0:
#             a.append(j)
#             a.append(i//j)
#     a.sort()
#     a5 = a[:5]
#     if len(a) < 5:
#         p = 0
#     else:
#         p = umnoj(a5)
#         if p%100 == 17 and p<=i:
#             print(p, max(a5))

a=0
for i in range(190201, 190260):
    c = 0
    a = []
    b =[]
    for j in range(1,int(i**0.5)+1):
        if j*j==i:
                c += 1
                a.append(j)
        elif i%j==0:
                c += 2
                a.append(j)
                a.append(i//j)
    for x in a:
        if x%2==0:
            b.append(x)
    b.sort(reverse=True)
    if len(b)==4:
        print(*b[:2])
