from sys import stdin
n, per = map(int,input().split())
total = []
for i in range(n):
    lista = list(map(int, stdin.readline().split()))
    n = max(lista)
    total.append(n**2)
res = sum(total)%per
print(res)
