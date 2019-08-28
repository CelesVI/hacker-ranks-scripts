from sys import stdin
from collections import Counter

n = int(input())
seta = Counter(list(map(int, stdin.readline().split())))
for key,value in seta.items():
    if (value==1):
        print(key)
