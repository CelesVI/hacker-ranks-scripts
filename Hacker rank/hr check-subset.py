from sys import stdin
n = int(input())
for i in range(n):
    m = int(input())
    a = set(map(int, stdin.readline().split()))
    o = int(input())
    b = set(map(int, stdin.readline().split()))
    print(a.issubset(b))
