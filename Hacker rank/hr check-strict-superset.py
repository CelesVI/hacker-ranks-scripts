from sys import stdin
a = set(map(int, stdin.readline().split()))
b= True
for i in range(int(input())):
    seta = set(map(int, stdin.readline().split()))
    if a.issuperset(seta):
        pass
    else:
        b = False
        break
print(b)
