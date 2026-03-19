import sys
sys.setrecursionlimit(10**9)
def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n-1)
print((f(2024)-5*f(2023))/f(2022))
