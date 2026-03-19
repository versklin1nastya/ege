for a in range(1, 10000):
    s = []
    for x in range(1,1000):
            if not ((x%25==0) <= ((x%a!=0) <= (x%60!=0))):
                s.append(0)
            else:
                s.append(1)
    if all(i == 1 for i in s):
        print(a)

# a = [i for i in range(1000)]
# p = [i for i in range(8, 12)]
# q = [i for i in range(4, 30)]
# for a in range(1000):
#     f = False
#     for x in range(10000):
#             if ((x & 76 !=0) <= ((x & 10 ==0) <= (x & a !=0))):
#                 f =  True
#                 break
#     if f:
#         print(a)
