from sys import stdin
happiness = 0
n,m = map(int, input().split())
lista = list(map(int, stdin.readline().split()))
A = set(map(int, stdin.readline().split()))
B = set(map(int, stdin.readline().split()))
for i in lista:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
print(happiness)
