x = 0
r = 0
k = 0
for i in open('9_27621.csv'):
    s = list(map(int, i.split(';')))
    k += 1
    s1 = set(s)
    # for i in s1:
    #     if s.count(i)==3:
    #         x = i
    if len(s1) == len(s) and sum(s) - max(s) - min(s) == max(s) - min(s):
        print(k)
