from sys import stdin
n = int(input())
lista = list(map(int, stdin.readline().split()))
m = int(input())
listb = list(map(int, stdin.readline().split()))
seta, setb = set(lista), set(listb)
setc = seta.union(setb)
print (len(list(setc)))
