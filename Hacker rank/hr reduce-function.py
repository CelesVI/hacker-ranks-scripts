from fractions import gcd
num = int(input())
f,g = [], []
for i in range(num):
    tof,tog = input().split()
    f.append(tof)
    g.append(tog)
print(gcd (f, g))
