def f(n, m, p):
    if n + m >= 211:
        return p%2==0
    if p==0:
        return 0
    h = [f(n + 1, m, p - 1), f(n * 2, m, p - 1), f(n, m + 1, p - 1), f(n, m * 2, p - 1)]
    return any(h) if p%2==1 else all(h)

print([i for i in range(1, 194)if f(17, i, 2)])
print([i for i in range(1, 194)if not f(17, i,1) and f(17, i,3)])
print([i for i in range(1, 194)if not f(17, i,2) and f(17, i,4)])

# def f(n, p):
#     if n <= 30:
#         return p%2==0
#     if p==0:
#         return 0
#     h = [f(n- 3, p - 1), f(n - 5, p - 1), f(n//4, p - 1)]
#     return any(h) if p%2==1 else all(h)
#
# print([i for i in range(1000, 30, -1)if f(i, 2)])
# print([i for i in range(1000, 30, -1)if not f(i,1) and f(i,3)])
# print([i for i in range(1000, 30, -1)if not f(i,2) and f(i,4)])
