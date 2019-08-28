from sys import stdin
x = int(input())
seta = list(map(str, stdin.readline().split()))
y = int(input())
setb = list(map(str, stdin.readline().split()))
seta = set(seta)
setb = set(setb)
setc = seta.difference(setb)
print(len(list(setc)))
