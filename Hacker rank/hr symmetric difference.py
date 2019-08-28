from sys import stdin
x = int(input())
seta = list(map(int, stdin.readline().split()))
y = int(input())
setb = list(map(int, stdin.readline().split()))
seta, setb = set(seta), set(setb)
setc, setd = setb.difference(seta) ,seta.difference(setb) 
lista, listb = list(setc), list(setd)
listc = lista + listb
listc.sort()
for i in range(len(listc)):
    print(listc[i])
