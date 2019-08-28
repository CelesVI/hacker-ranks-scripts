from sys import stdin
x = int(input())
seta = list(map(str, stdin.readline().split()))
y = int(input())
setb = list(map(str, stdin.readline().split()))
seta, setb = set(seta), set(setb)
lista = seta^setb
print(len(lista))
